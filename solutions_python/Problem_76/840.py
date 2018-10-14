#!/usr/bin/python

import sys

def patrick(candies):
	s = 0
	for c in candies:
		s = (s | c) & ~(s & c)
	return s

def sean(candies):
	return sum(candies)

def solve(candies, i, p, s):
	# basis case
	if len(p) + len(s) == len(candies):
		if len(p) == 0 or len(s) == 0:
			return 0
		sumPatrick = patrick(p)
		sumSean = patrick(s)
		if sumPatrick == sumSean:
			return sum(p)
		else:
			return 0
	
	p1 = p[:]
	p1.append(candies[i])
	a = solve(candies, i+1, p1, s)
	s1 = s[:]
	s1.append(candies[i])
	b = solve(candies, i+1, p, s1)

	if a==0 and b==0:
		return "NO"
	if a > b:
		return a
	return b


f = open(sys.argv[1], 'r')
cases = int(f.readline())
for c in range(1, cases+1):
	numCandies = int(f.readline())
	candies = [int(x) for x in f.readline().split()]
	assert(len(candies) == numCandies)
	print("Case #%d: %s" % (c, str(solve(candies, 0, [], []))))
