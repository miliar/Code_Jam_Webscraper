#!/usr/bin/python2

import sys, os, string, re

in_file = sys.stdin
T = int(in_file.readline())
for case_num in range(T):
	s = in_file.readline().strip()

	h = {}
	for ch in s:
		h[ch] = None
	base = len(h.keys())
	if base == 1:
		base = 2

	val = 1
	zero_assigned = False
	answer = 0
	for ch in s:
		if h[ch] == None:
			if val == 2:
				if not zero_assigned:
					h[ch] = 0
					zero_assigned = True
				else:
					h[ch] = 2
					val += 1
			else:
				h[ch] = val
				val += 1
		answer = base*answer + h[ch]

	print 'Case #%d: %s' % (case_num+1, str(answer))
