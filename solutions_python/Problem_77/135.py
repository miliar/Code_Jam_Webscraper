#!/usr/bin/python

# D. GoroSort

import math
import sys

f = sys.stdin
T = int(f.readline())

for x in range(1, T+1):
	f.readline()
	list = [int(e) for e in f.readline().split()]
	list2 = []
	list2.extend(list)
	list2.sort()

	y = 0.0
	for i in range(len(list)):
		if list[i] != list2[i]:
			y += 1.0

	print "Case #%d: %f" % (x, y)
