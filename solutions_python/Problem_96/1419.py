#!/usr/bin/env python2
import sys, os
# Cases
t = int(sys.stdin.readline())
threshL2 = []

for i in xrange(t):
	case = map(int, sys.stdin.readline().split())
	thresh1 = case[2] * 3 - 2
	if case[2] < 3:
		thresh2 = case[2]
	else:
		thresh2 = case[2] * 3 - 4

	maxDev = case[1]
	numWinners = 0
	for j in xrange(3, case[0] + 3):
		if case[j] >= thresh1:
			numWinners += 1
		elif case[j] >= thresh2 and maxDev > 0:
			numWinners += 1
			maxDev -= 1
	print "Case #%d: %d" % (i+1, numWinners)
