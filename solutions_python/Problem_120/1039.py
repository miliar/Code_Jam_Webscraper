#!/usr/bin/env python2.7
import math


N = int(raw_input())

for n in xrange(N):
	r, t = map(float, raw_input().split())
	count = math.floor(((-((2*r) - 1)) + math.sqrt((((2*r) - 1)**2) + 8*t)) / 4.0)
	if (2*(count**2) + (2*r - 1)*count - t > 0):
		count -= 1
	print "Case #%d:" % (n+1), int(count)

