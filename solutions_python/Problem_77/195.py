#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Code to solve Google Code Jam problem "C. GoroSort". Qualification round of may 07 2011."""

import sys

def goroSort(inName):
	"""Starts the resolution of the test cases."""
	if inName.find(".in") > 0:
		outName = inName.replace(".in", ".out")
	else:
		outName = inName + ".out"
	
	with open(inName) as fIn:
		with open(outName, "w") as fOut:
			cases = int(fIn.readline())
			for i in xrange(1, cases + 1):
				solveCase(i, fIn, fOut)

def solveCase(case, fIn, fOut):
	"""Solves a test case."""
	fIn.readline() # elements in the arrays, ignore
	
	data = fIn.readline().split()
	array = []
	for item in data:
		array.append(int(item))
	
	sortedItems = 0
	for i, item in enumerate(sorted(array)):
		if array[i] == item:
			sortedItems += 1

	solution = len(array) - sortedItems
	print "Case #{0}: {1:.6f}".format(case, solution)
	fOut.write("Case #{0}: {1:.6f}\n".format(case, solution))

if __name__ == "__main__":
	goroSort(sys.argv[1])
