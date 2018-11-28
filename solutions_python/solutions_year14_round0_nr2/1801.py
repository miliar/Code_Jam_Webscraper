#!/usr/bin/python

import sys

T = int(sys.stdin.readline().strip())

for i in xrange(T):
	C, F, X = map(float,sys.stdin.readline().strip().split())
	rate = 2.0
	time = 0.0
	total_time = 0.0
	while(True):
		expected_time = X / rate
                future_expected_time = (C/rate)+((X)/(rate+F))
                if expected_time < future_expected_time:
			total_time = total_time + expected_time
		        break
                time = C / rate	#BUY
		rate = rate + F
		total_time = total_time + time
	
	print "Case #%d: %.7f" %(i+1, total_time)
