#!/usr/bin/env python

import sys

def missing (s):
	standing_up = 0
	missing = 0
	(max_shy, shyness) = s.split()
	max_shy = int (max_shy)
	for n, xn in enumerate (shyness):
		xn = int (xn)

		if (standing_up >= n):
			pass
		elif (xn > 0):
			missing += (n - standing_up)
			standing_up += (n - standing_up)

		standing_up += xn

	return missing



def solve (num):
	print ("Case #%d: %d" % (num, missing (sys.stdin.readline())))



num_cases = int (sys.stdin.readline())

for case in range (1, num_cases + 1):
	solve (case)
