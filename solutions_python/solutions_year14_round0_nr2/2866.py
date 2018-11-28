#!/usr/bin/env python

import sys

f = open(sys.argv[1])
cases = f.readlines()
f.close()

len_cases = int(cases[0])
for i in range(1, len_cases+1):
	speed = 2.000000
	case = cases[i].split()
	cost = float(case[0])
	rendement = float(case[1])
	goal = float(case[2])
	etime = 0.000000
	while(cost/speed+goal/(speed+rendement) < goal/speed):
		etime = etime + cost/speed
		speed = speed + rendement
	if cost/speed + goal/(speed+rendement) < goal/speed:
		etime = etime + cost/speed
		speed = speed + rendement
	print "Case #%d: %.7f" % (i, etime+goal/speed)