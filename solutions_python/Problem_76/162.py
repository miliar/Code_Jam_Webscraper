import sys

with open(sys.argv[1]) as f:
	T = int(f.readline())
	for testcase in xrange(T):
		N = int(f.readline())
		C = [int(x) for x in f.readline().split()]
		
		s = 0
		t = 0
		for c in C:
			s ^= c
			t += c
		
		if s == 0:	
			answer = t - min(C)
		else:
			answer = 'NO'
			
		print 'Case #%d:' % (testcase + 1), answer