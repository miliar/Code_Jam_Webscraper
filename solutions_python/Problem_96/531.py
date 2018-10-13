#!/usr/bin/python

import sys
sys.stdin.readline()

for case, line in enumerate(sys.stdin.readlines(), 1):
	vals = [int(x) for x in line.split()]
	N, S, p = vals[:3]
	scores = vals[3:]
	count = 0
	for score in scores:
		third = score // 3
		mod = score % 3
		if score < 2 or score > 28:
			maxval = min(third + mod, 10)
		else:
			maxval = third + (mod > 0)
			if maxval == p - 1 and S > 0 and mod != 1:
				S -= 1
				maxval += 1
		if maxval >= p:
			count += 1
	print("Case #%d: %d" % (case, count))
