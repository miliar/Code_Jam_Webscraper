#!/usr/bin/env python

import sys

for i in range(int(sys.stdin.readline())):
	params = sys.stdin.readline().strip().split(' ')
	chicks = sys.stdin.readline().strip().split(' ')
	speeds = sys.stdin.readline().strip().split(' ')

	n = int(params[0])
	k = int(params[1])
	b = int(params[2])
	t = int(params[3])

	bad = []
	swaps = 0
	for j in range(n -1, -1,  -1):
		if k <= 0:
			continue

		if int(chicks[j]) + t * int(speeds[j]) < b:
			bad.append(chicks[j])
		else:
			swaps += len(bad)
			k -= 1

	if k > 0:
		print "Case #%i: IMPOSSIBLE" % (i+1)
	else:

		print "Case #%i: %i" % (i+1, swaps)
