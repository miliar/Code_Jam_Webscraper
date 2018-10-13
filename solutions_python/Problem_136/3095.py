#!/usr/bin/env python

import io

fil = open("input.txt")

cases = int(fil.readline())

for n in range(cases):
	time = 0.0
	cookies = 0.0
	rate = 2.0
	[c, f, x] = [float(num) for num in fil.readline().split(" ")]

	while cookies < x:
		should_buy = ((c / rate) + (x / (rate + f))) < (x / rate)
		if should_buy is True:
			time = time + c / rate
			rate = rate + f
		else:
			time = time + x / rate
			cookies = x
			
	print "Case #%d: %f" % ((n + 1), time)
