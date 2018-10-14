import sys

stdin = sys.stdin

T = int(stdin.readline())

for t in xrange(T):
	s = stdin.readline().split()
	N = int(s[0])
	M = int(s[1])
	
	mkdirs = 0
	F = dict()
	
	for n in xrange(N):
		S = stdin.readline().split('/')[1:]
		f = F
		for s in S:
			s = s.strip()
			if not f.has_key(s):
				f[s] = dict()
			f = f[s]
		
	for m in xrange(M):
		S = stdin.readline().split('/')[1:]
		f = F
		for s in S:
			s = s.strip()
			if not f.has_key(s):
				f[s] = dict()
				mkdirs += 1
			f = f[s]
	print "Case #%d: %d" %(t+1, mkdirs)
