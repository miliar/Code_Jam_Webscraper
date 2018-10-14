#!/usr/bin/python

import sys

def isInHarmony(f, freqs):
	for _f in freqs:
		if (f % _f) != 0 and (_f % f) != 0:
			# print("_f=%d f=%d" % (_f, f))
			return False
	return True

def solve(low, high, freqs):
	# print("====")
	# print(str(freqs))
	for f in range(low, high+1):
		if isInHarmony(f, freqs):
			return str(f)
	return "NO"

f = open(sys.argv[1], 'r')
for c in range(1, int(f.readline())+1):
	# read case
	v = [int(x) for x in f.readline().split()]
	(numOthers, low, high) = (v[0], v[1], v[2])
	freqs = [int(x) for x in f.readline().split()]
	assert(len(freqs) == numOthers)
	# solve and print result
	print("Case #%d: %s" % (c, solve(low, high, freqs)))
