#!/usr/bin/env python

import sys, math


def solve (casenum, r, vol):
	result = 0
	while (vol):
		# draw one ring
		# a_ring = math.pi * ((r+1) * (r+1) - r * r)
		# vol_needed = a_ring / math.pi
		vol_needed = ((r+1) * (r+1) - r * r)
		#print >>sys.stderr, "ring: (%lu - %lu), a: %lf, v: %lf" % (r+1, r, math.pi * ((r+1) * (r+1) - r * r), ((r+1) * (r+1) - r * r))
		if vol_needed > vol: break
		result += 1
		r += 2
		vol -= vol_needed
		
	print "Case #%d: %s" % (casenum, result)


num_testcases = int (sys.stdin.readline())

for case in range (1, num_testcases+1):
	(r, t) = map (int, sys.stdin.readline().split())
	solve (case, r, t)
