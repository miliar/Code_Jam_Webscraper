#!/usr/bin/env python

cases = int(raw_input())

for case in range(cases):
	(R, k, N) = map(int, raw_input().split())
	g = map(int, raw_input().split())

	num_groups = [0] * N

	# Pre-calculate number of groups for each starting point and
	# number of seats that would be filled
	for i in range(N):
		filled = 0
		for j in xrange(N):
			if filled + g[(i + j) % N] > k:
				break
			filled += g[(i + j) % N]
		num_groups[i] = (j, filled)

	# Step through
	pos = 0
	money = 0
	for run in range(R):
		t = num_groups[pos % N]
		pos += t[0]
		money += t[1]

	print "Case #%d: %d" % (case + 1, money)
