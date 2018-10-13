#!/usr/bin/python

T = int(raw_input())
for test in xrange(T):
	n = int(raw_input())
	l = sorted(map(int, raw_input().split()))
	ans = 'NO'
	if reduce(lambda x, y: x ^ y, l) == 0:
		ans = sum(l[1:])
	print "Case #%d: %s" % (test + 1, ans)
