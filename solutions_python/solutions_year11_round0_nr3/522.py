#!/usr/bin/env python

import sys
import itertools
from copy import deepcopy

def patrickAdd(l):
	patrickSum = 0
	for i in l:
		patrickSum ^= i
	return patrickSum

def solve(n, c):
	maxSum = 0
	#print "++> ALL: %s" % (c)
	for i in range(len(c)-1):
		#print "  SIZE: %s" % (i+1)
		#for setP in itertools.permutations(c, i+1):
		for setP in itertools.combinations(c, i+1):
			P = list(setP)
			S = deepcopy(c)
			for i in P:
				S.pop(S.index(i))
			#print "    SET P+S: %s + %s" % (P, S)
			countP = patrickAdd(P)
			countS = patrickAdd(S)
			#print "    SUM P=S: %s = %s" % (countP, countS)
			if countS == countP:
				trueCount = sum(S)
				if maxSum < trueCount:
					maxSum = trueCount
				#print "      Bingo %s --> %s" % (trueCount, maxSum)
		#print "  MaxSum = %s" % (maxSum)

	return maxSum if maxSum > 0 else "NO"

def main(infile):
	n = int(infile.readline())
	for i in range(n):
		cmd = infile.readline().split()
		m = int(cmd.pop(0))
		candies = [int(x) for x in infile.readline().split()]
		print 'Case #%s: %s' % (i+1, solve(m, candies))

main(sys.stdin)
