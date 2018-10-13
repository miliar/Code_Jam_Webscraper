#!/usr/bin/python

import sys
from itertools import permutations

		
def sumup(candies):
	s = candies[0]
	for c in candies[1:]:
		s ^= c
	return s

def solve(candies):
	pool = tuple(sorted(candies))
	n = len(pool)
	rangen = range(n)
	totalsum = sum(pool)
	for l in range(1, n):
    		for indices in permutations(rangen, l):
        		if sorted(indices) == list(indices):
            			a = tuple(pool[i] for i in indices)
            			b = tuple(pool[i] for i in rangen if not i in indices)
				if sum(b) < totalsum/2:
					return "NO"
				if sumup(a) == sumup(b):
					return sum(b)
	return "NO"


T = int(sys.stdin.readline())
lines = sys.stdin.readlines()

for t in range(T):
	candies = [int(x) for x in lines[t*2+1].split()]
	sol = solve(candies)
	print "Case #" + str(t+1) + ": " + str(sol)

