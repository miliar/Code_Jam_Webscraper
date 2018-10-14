#!/usr/bin/python

# B. Cookie clicker

import sys



f = sys.stdin
T = int(f.readline())

for t in range(1, T+1):

	C, F, X = map(float, f.readline().strip().split())

	answer = 0.0
	productionRate = 2.0

	while X / productionRate > C / productionRate + X / (productionRate + F):
		answer += C / productionRate
		productionRate += F

	answer += X / productionRate

	print "Case #%d: %f" % (t, answer)
