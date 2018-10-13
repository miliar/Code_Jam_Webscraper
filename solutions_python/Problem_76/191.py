#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Code to solve Google Code Jam problem "C. Candy Splitting". Qualification round of may 07 2011"""

import sys

def splitCandies(inName):
	"""Splits the candies!"""
	if inName.find(".in") > -1:
		outName = inName.replace(".in", ".out")
	else:
		outName = inName + ".out"

	with open(inName) as fIn:
		with open(outName, "w") as fOut:
			cases = int(fIn.readline())
			for i in xrange(1, cases + 1):
				solveCase(i, fIn, fOut)

def solveCase(case, fIn, fOut):
	"""Solves a test case"""
	fIn.readline() # amount of candies, ignore
	data = fIn.readline().split()

	patrickSum = 0
	smallerCandy = 0
	sum = 0
	for i, candy in enumerate(data):
		tmp = int(candy)
		if i == 0:
			smallerCandy = tmp
		else:
			smallerCandy = min(tmp, smallerCandy)
		sum += tmp
		patrickSum ^= tmp

	if patrickSum == 0:
		response = sum - smallerCandy
	else:
		response = "NO"
	print "Case #{0}: {1}".format(case, response)
	fOut.write("Case #{0}: {1}\n".format(case, response))

if __name__ == "__main__":
	splitCandies(sys.argv[1])
