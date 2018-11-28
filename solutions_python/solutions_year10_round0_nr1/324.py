#!/usr/bin/env python

import sys, math

cases = int(sys.stdin.readline())
for case_no in xrange(1, cases + 1):
	nums = sys.stdin.readline().split()
	N = int(nums[0])
	K = int(nums[1])

	val = math.pow(2.0, N)
	print 'Case #%d:' % case_no,
	if K % val == (val - 1):
		print 'ON'
	else:
		print 'OFF'
