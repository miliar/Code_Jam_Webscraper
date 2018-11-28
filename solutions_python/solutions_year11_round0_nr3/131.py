#!/usr/bin/python

# C. Candy Splitting

import math
import sys

def xor(list):
	result = 0
	for e in list:
		result ^= e
	return result

f = sys.stdin
T = int(f.readline())

for x in range(1, T+1):
	f.readline()
	list = [int(e) for e in f.readline().split()]
	list.sort()

	if xor(list) == 0:
		y=0
		#for i in range(1, len(list)):
		for i in range(1, len(list)):
			if xor(list[:i]) == xor(list[i:]):
				y = max([y, sum(list[:i]), sum(list[i:])])
	else:
		y = "NO"

	print "Case #%d: %s" % (x, y)
