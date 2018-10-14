
fi = open('A-small.in','r')

def inp(fi):					#change to file based io quickly
	return fi.readline().rstrip('\n\r')
	
def search(data,i,b,s,c):
	if (i >= len(data)):
		if b in s:
			c += 1
		return c
		
	for x in xrange(len(data[i])):
		b += data[i][x]
		if b in s:
			c = search(data,i+1,b,s,c)
		b = b[0:i]
	return c
	
def solve(s,L):
	token = 0
	state = 'scan'
	buf = ''
	data = []
	i = -1
	while (token < L):
		i+=1
		if s[i] == '(':
			assert(state =='scan')
			state = 'bracket'
			buf = ''
		elif s[i] == ')':
			data.append(buf)
			assert(state == 'bracket')
			state = 'scan'
			token += 1
		else:
			if state == 'scan':
				data.append(s[i])
				token += 1
			elif state == 'bracket':
				buf += s[i]
	return data

line = inp(fi)
line = line.split(' ')
L = int(line[0])
D = int(line[1])
N = int(line[2])

words = dict()

for x in xrange(D):
	a = inp(fi)
	for y in xrange(len(a)+1):
		words[a[0:y]] = 1

f = open('alien.out','w')
a = 0
for x in xrange(N):
	a+=1
	d = solve(inp(fi),L)
	#print d,'------->'
	c = search(d,0,'',words,0)
	#print s,'------->'
	print >>f,"Case #"+str(a)+": "+str(c)
	print "Case #"+str(a)+": "+str(c)
f.close()
fi.close()