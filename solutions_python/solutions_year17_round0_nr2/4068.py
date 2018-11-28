def tidy(x):
	i = x
	while i != 1:
		if isTidy(i):
			return i
		else:
			i = zeroNumber(i)
			i = i - 1
	return 1
	
def isTidy(x):
	n = str(x)
	v = n[0]
	for i in xrange(1,len(n)):
		if n[i] < v:
			return False
		v = n[i]
	return True

def zeroNumber(x):
	l = []
	s = str(x)
	for i in xrange(0,len(s)):	
		l.append(int(s[i]))
	v = l[0]
	for i in xrange(1,len(l)):
		if l[i] < v:
			for j in xrange(i,0,-1):
				if l[j] != v or j == 1:
					for k in range(j, len(l)):
						l[k] = 0
					s = map(str, l)
					s = ''.join(s)
					return int(s)
		else:
			v = l[i]
				
						
# Main
t = input()
n = []

for i in range(0,t):
	n.append(input())
	
for i in range(0,t):
	print 'Case #%s: %s' % (i+1, tidy(n[i]))
