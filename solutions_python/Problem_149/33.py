#!/usr/bin/python

import sys

TT = int(sys.stdin.readline())

for T in xrange(1,TT+1):
	N = int(sys.stdin.readline())
	a = map(int, sys.stdin.readline().split())

	srt = sorted(a)
	ans = 0
	for x in srt:
		p = filter(lambda (i,v): v==x ,enumerate(a))[0][0]
		ans += min(p, len(a)-p-1)
		a = a[:p] + a[p+1:]

	print "Case #%d: %d" % (T, ans)


