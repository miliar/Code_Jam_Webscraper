#!/usr/bin/env python
# Fair square checker

import gmpy

def check_range(start, end):
	qty = 0
	i = start

	for i in xrange(start, end+1):
		if gmpy.is_square(i):
			strn = str(i)
			if strn == strn[::-1]:
				n = str(gmpy.sqrt(i))
				if n == n[::-1]:
					qty += 1
		i += 1

	return qty

def read_range():
	rangestr = raw_input().strip().split(" ")
	return (int(rangestr[0]), int(rangestr[1]))


# Get cases quantity
cases = int(raw_input())

for i in xrange(1, cases+1):
	start, end = read_range()

	print "Case #%d: %d" % (i, check_range(start, end))
