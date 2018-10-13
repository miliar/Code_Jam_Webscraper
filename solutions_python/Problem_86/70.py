#!/usr/bin/python

T = int(raw_input())
for t in xrange(T):
	n, l, h = map(int, raw_input().split())
	a = map(int, raw_input().split())
	ans = "NO"
	for f in xrange(l, h + 1):
		ok = True
		for item in a:
			if item % f != 0 and f % item != 0:
				ok = False
		if ok:
			ans = str(f)
			break
	print "Case #%d: %s" % (t + 1, ans)
