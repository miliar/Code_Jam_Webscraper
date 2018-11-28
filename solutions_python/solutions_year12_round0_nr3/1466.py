#!/usr/bin/python

import sys

# another brute force approach. feeling brutal today.


def shift_stuff (x):
	o = str (x)
	xl = len (o)

	for l in range (1, xl):
		uut = o[xl - l:] + o[0:xl - l]
#		print "testing", x, y
		if uut[0] == '0': continue
		y = int (uut)
		(x, y) = sorted ((x, y))

		if (x == y) or (y > lst) or (x < fst):
			continue

		all_pairs.add ((x, y))


num_testcases = int (sys.stdin.readline())

for n in range (1, num_testcases+1):
	all_pairs = set()
	line = sys.stdin.readline().split()
	fst = int (line[0])
	lst = int (line[1])

	for cand in range (fst, lst+1):
		shift_stuff (cand)

#	print all_pairs
#	print "num pairs: ", len (all_pairs)

	print "Case #%d: %d" % (n, len (all_pairs))



