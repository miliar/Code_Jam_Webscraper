#! /usr/bin/env pypy
T = input()
for i in xrange(1, T+1):
	A, B = map(int, raw_input().split())
	L = len(str(A))
	npairs = 0
	for n in xrange(A, B):
		x, y = 1, 10 ** L
		s = set()
		for j in xrange(1, L):
			x *= 10
			y //= 10
			m = n // x + n % x * y
			if n < m <= B:
				s.add(m)
		npairs += len(s)
	print 'Case #%d: %d' % (i, npairs)
