#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

input = sys.stdin.readlines()
cases = int(input[0])

for i in range(1, cases+1):
	values = map(float,input[i].split())
	C, F, X = values[0], values[1], values[2]

	time = 0
	rate = 2

	while(1):
		t = time + X/rate
		t2 = time + C/rate + X/(rate+F)

		time += C/rate
		rate += F

		if t2 >= t:
			print "Case #%d: %.7f" % (i, t)
	 		break