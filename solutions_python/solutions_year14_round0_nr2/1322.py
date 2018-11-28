#!/usr/bin/python


T = int(raw_input())

for tc in xrange(1, T + 1):
	c, f, x = map(float, raw_input().split())
	
	prod = 2.0
	elapsed = 0
	while x / prod > (c / prod + x / (prod + f)):
		elapsed += c / prod
		prod += f
	elapsed += x / prod
	print "Case #%d: %.7f" % (tc, elapsed)
