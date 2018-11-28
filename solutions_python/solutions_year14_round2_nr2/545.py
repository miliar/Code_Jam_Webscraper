#!/usr/bin/python
# Obviusly a work in progress

import sys

def solve():
	A, B, K = map(int, sys.stdin.readline().split())
	wins = 0
	for a in xrange(0, A):
		for b in xrange(0, B):
			if a & b < K:
				wins += 1
	return wins 

num = int(sys.stdin.readline())

for case in range(1, num + 1):
    print "Case #%d: %d" % (case, solve())
