#! /usr/bin/env python

# python 2.7
#usage: cat input | this_program > output

from __future__ import division
import sys
import math


num_testcases = int(sys.stdin.readline())

### main
for case in range(1, num_testcases + 1):
	C, F, X = map(float, sys.stdin.readline().split())
	time = 0.0
	rate = 2.0
	#As long as the condition X/rate <= C/rate + X/(rate + F)
	#holds where rate = 2. + n * F (n beeing the number of buys
	#already done) it makes sense to do another buy.
	#So we calculate the number of buys as
	num_buys = int(math.ceil(((X-C)*F/C-2.)/F))
	for _ in range(num_buys):
		time += C / rate
		rate += F
	time += X / rate
	print "Case #%i: %.9f" %(case, time)
