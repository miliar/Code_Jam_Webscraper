#! /usr/bin/env python
import sys
import math

T = int(sys.stdin.readline())

for t in range(1, T+1):
	C, F, X = map(float, sys.stdin.readline().split())
	numBuy = int(math.ceil(X / C - 1 - 2.0 / F))
	numBuy = 0 if numBuy < 0 else numBuy

	time = 0.0
	for i in range(numBuy):
		time += C / (2.0 + i * F)
	time += X / (2.0 + numBuy * F)

	print "Case #{0}: {1}".format(t, time)