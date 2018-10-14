from math import sqrt,ceil,floor
def fair(s):
	l = len(s)
	for i in range(l/2):
		if s[i] != s[l-i-1]:
			return False
	return True
		
T = int(raw_input())
for i in range(T):
	A,B = map(int, raw_input().split())
	c = 0
	for n in range(int(ceil(sqrt(A))),int(floor(sqrt(B)))+1):
		if fair(str(n)) and fair(str(n**2)):
			c+=1
	print 'Case #%d: %d' % (i+1, c)
