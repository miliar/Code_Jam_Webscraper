def solve(lawn):
	n, m = len(lawn), len(lawn[0])
	t = lawn[:]
	for i in xrange(n): ## row
		if set(lawn[i]) == set([1]):
			t[i] = [2] * m
	for j in xrange(m): #col
		if set([lawn[i][j] for i in xrange(n)]) == set([1]):
			for i in xrange(n):
				t[i][j] = 2
	return 'YES' if t == [[2]*m]*n else 'NO'

TC = input()
for T in xrange(TC):
	n, m = map(int, raw_input().split())
	lawn = [map(int, raw_input().split()) for _ in xrange(n)]
	print 'Case #%d: %s' % (T+1, solve(lawn))

