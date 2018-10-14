#!/usr/bin/env python

numTests = int(raw_input())

for testNo in xrange(1, numTests + 1):
	print 'Case #{0}:'.format(testNo),
	c, f, x = [float(i) for i in raw_input().split()]
	production = 2.0
	totalTime = 0
	while x / production > (c / production + x / (production + f)):
		totalTime += c / production
		production += f
	print totalTime + x / production
