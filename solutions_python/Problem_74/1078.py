import sys

f = open(sys.argv[1])

n = int(f.readline())
for testcase in range(1, n+1):
	s = f.readline().split()
	s.pop(0)	
	O = filter(bool, [int(s[i+1]) if s[i]=='O' else None for i in range(0, len(s), 2)])
	B = filter(bool, [int(s[i+1]) if s[i]=='B' else None for i in range(0, len(s), 2)])
	S = [(s[i], int(s[i+1])) for i in range(0, len(s), 2)]
	c,o,b = 0,1,1
	while S:
		c+=1
		p = 0
		if O:
			if O[0] != o:
				o+=(1 if O[0]>o else -1)
			elif S[0] == ('O', o):
				p = 1
				S.pop(0)
				O.pop(0)
		
		if B:
			if B[0] != b:
				b+=(1 if B[0]>b else -1)
			elif S[0] == ('B', b) and p==0:
				S.pop(0)
				B.pop(0)
	
	print 'Case #%d: %d' % (testcase, c)
