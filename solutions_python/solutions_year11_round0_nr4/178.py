#!/usr/bin/python

T = int(raw_input())
for t in xrange(T):
	n = int(raw_input())
	L = map(int, raw_input().split())
	ans = len(L)
	for i, v in enumerate(L):
		if i == v - 1:
			ans -= 1
	print "Case #%d: %d.000000" % (t + 1, ans)
