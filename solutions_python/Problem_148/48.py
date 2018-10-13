#!/usr/bin/python

import sys

TT = int(sys.stdin.readline())

for T in xrange(1,TT+1):
	N, X = map(int, sys.stdin.readline().split())
	a = sorted(map(int, sys.stdin.readline().split()))

	ans = 0
	i, j = 0, N-1
	while i<=j:
		if a[i]+a[j] <= X:
			i += 1
		j -= 1
		ans += 1

	print "Case #%d: %d" % (T, ans)


