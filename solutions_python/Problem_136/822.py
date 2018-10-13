#! /usr/bin/python

import sys

trials = int(sys.stdin.readline())

for rnd in range(trials):
	cookies_per_second = 2.0
	C, F, X = [ float(x) for x in sys.stdin.readline().split(" ") ]
	time = 0
	while 1:
		run1 = (X / cookies_per_second)
		run2 = (C / cookies_per_second) + (X / (cookies_per_second + F))
		if (time + run1 < time + run2):
			time += run1
			break
		else:
			time += (C / cookies_per_second)
			cookies_per_second += F
	print 'Case #%d: %.7f' % (rnd + 1, time)
