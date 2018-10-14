#!/usr/bin/env python

import sys

cases = int(sys.stdin.readline())

for case in xrange(1, cases + 1):
	print "Case #%d:" % case,
	line = sys.stdin.readline().strip()
	N, Pd, Pg = [int(val) for val in line.split()]
	if Pg == 0 and Pd != 0:
		print 'Broken'
		continue
	if Pg == 100 and Pd != 100:
		print 'Broken'
		continue
	factors = 100
	if Pd % 5 == 0:
		factors /= 5
		Pd /= 5
	if Pd % 5 == 0:
		factors /= 5
		Pd /= 5
	if Pd % 2 == 0:
		factors /= 2
		Pd /= 2
	if Pd % 2 == 0:
		factors /= 2
		Pd /= 2
	if factors > N:
		print 'Broken'
		continue

	print 'Possible'

