#!/usr/bin/python
import sys, math, bisect

res = []

for i in range(1, int(math.sqrt(10**14)+1)):
	s = str(i)
	s2 = str(i*i)
	if s==s[::-1] and s2==s2[::-1]:
		res.append(i*i)

t = int(sys.stdin.readline())

for test in range(t):
	a,b = [int(x) for x in sys.stdin.readline().split()]
	xa = bisect.bisect_left(res, a)
	xb = bisect.bisect_right(res, b)
	print "Case #%d: %d" % (test + 1, xb-xa)