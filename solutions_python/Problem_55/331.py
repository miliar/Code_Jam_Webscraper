#!/usr/bin/env python

import sys, math

cases = int(sys.stdin.readline())
for case_no in xrange(1, cases + 1):
	print 'Case #%d:' % case_no,
	R, k, N = [int(v) for v in sys.stdin.readline().strip().split()]
	vals = [int(v) for v in sys.stdin.readline().strip().split()]
	#print R, k, N

	value = []
	next = []
	ends = [0, 0]
	cval = vals[0]
	# work out values for each point
	while ends[0] < len(vals):
		while True:
			#print ends, cval
			# if next is the end, set so it would be the start
			if ends[1] + 1 == len(vals):
				ends[1] = -1
			# if the next won't fit, stop here
			if cval + vals[ends[1] + 1] > k:
				break
			# if the next one is the current one, we can't use it
			if ends[1] + 1 == ends[0]:
				break
			ends[1] += 1
			cval += vals[ends[1]]

		value.append(cval)
		next.append(ends[1] + 1)
		# remove left value
		if ends[1] == ends[0]:
			ends[1] += 1
			cval = vals[ends[1]]
		else:
			cval -= vals[ends[0]]
		ends[0] += 1

	#print vals
	#print value
	#print next

	seen = [False for val in vals]
	# progress until a point is seen again
	income = 0
	loc = 0
	time = 0
	while not seen[loc]:
		seen[loc] = True
		income += value[loc]
		loc = next[loc]
		time += 1
		if time == R:
			break
	#print income, 'init'

	# calculate value of the cycle
	cycle_val = 0
	cycle_len = 0
	for i in xrange(len(seen)):
		seen[i] = False
	pos = loc
	while not seen[pos]:
		seen[pos] = True
		cycle_val += value[pos]
		cycle_len += 1
		pos = next[pos]
	#print cycle_val, cycle_len, loc

	# work out number of repeats
	repeats = (R - time) / cycle_len
	#print vals
	#print repeats, R, time, cycle_len
	if repeats > 0:
		income += repeats * cycle_val

	# work out end bit
	if R - time > 0:
		left_over = (R - time) % cycle_len
		pos = loc
		for i in xrange(left_over):
			income += value[pos]
			pos = next[pos]
	print income
