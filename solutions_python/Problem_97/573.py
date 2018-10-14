import math
import sys

k = int(sys.stdin.readline())

for id, line in enumerate(sys.stdin):
	A, B = map(int, line.split())
	cnt = 0
	l = len(str(A))
	z = 10**(l-1)
	for n in xrange(A, B):
		m = n
		had = set()
		for _ in xrange(l-1):
			m = (m / 10) + (m % 10) * z
			if n < m <= B and (m not in had):
				cnt += 1
				had.add(m)
	print 'Case #%d: %s' % (id+1, cnt)
