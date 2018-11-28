import math
import sys

k = int(sys.stdin.readline())

d = {}
for i in xrange(0, 11):
	for j in xrange(0, 11):
		for k in xrange(0, 11):
			if abs(i-j) > 2 or abs(i-k) > 2 or abs(j-k) > 2: continue
			s = i+j+k
			m = max(i, j, k)
			strange = (abs(i-j) == 2 or abs(i-k) == 2 or abs(j-k) == 2)
			d[(s, strange)] = max(m, d.get((s, strange), 0))

for id, line in enumerate(sys.stdin):
	a = map(int, line.split())
	N, S, p = a[:3]
	t = a[3:]
	x = [[0 for _ in xrange(S+1)] for _ in xrange(N+1)]
	for i in xrange(1, N+1):
		for j in xrange(0, S+1):
			x[i][j] = x[i-1][j] + (d[(t[i-1], False)] >= p)
			if j > 0 and (t[i-1], True) in d:
				x[i][j] = max(x[i][j], x[i-1][j-1] + (d[(t[i-1], True)] >= p))
	print 'Case #%d: %s' % (id+1, x[N][S])
