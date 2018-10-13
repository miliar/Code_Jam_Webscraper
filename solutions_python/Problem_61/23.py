#!/usr/bin/python

_F = {}
def F(n,m):
	if n == 0 and m >= 0: return 1
	if n < 0: return 0
	if n > 0 and m == 0: return 0
	if (n,m) not in _F:
		ans = 0
		for i in xrange(n-1, n-m-1, -1):
			ans += F(i,m)
		_F[(n,m)] = ans
	return _F[(n,m)]

ans = [sum([F(i-j, j) for j in xrange(i+1)]) % 100003 for i in xrange(510)]

T = int(raw_input().strip())

for nCase in xrange(1, T+1):
	print "Case #%d: %d" % (nCase, ans[int(raw_input().strip())-1])
