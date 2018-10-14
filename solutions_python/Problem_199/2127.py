import fileinput

def flipk(start, s, k):
	i = 0
	for i in xrange(k):
		index = start+i
		if s[index] == '-':
			s[index] = '+'
		else:
			s[index] = '-'

def flip(s, k):
	# t is a copy of s
	t = s 
	res = 0
	i = 0
	for i in xrange(len(s)-k+1):
		e = s[i]
		if e == '-':
			flipk(i, s, k)
			res += 1
			
	if '-' in s[i:]:
		return "IMPOSSIBLE"
		
	else:
		return res
		
	
	
it = fileinput.input()
it.next()
num = 1
for line in it:
	s,k  = line.split(' ')
	k = int(k)
	s = list(s)
	print "Case #" + str(num) + ': ' + str(flip(s,k))
	num += 1
	
	
	