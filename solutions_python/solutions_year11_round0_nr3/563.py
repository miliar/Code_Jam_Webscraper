#!/usr/bin/env python

from __future__ import print_function

import sys

def calcSeanValue(candyList):

	leastValuableCandy = int(candyList[0])
	xorCandy = 0
	sumCandy = 0
	
	for i in candyList:
		candyValue = int(i)
		sumCandy = sumCandy + candyValue
		xorCandy = xorCandy ^ candyValue
		
		if (candyValue < leastValuableCandy):
			leastValuableCandy = candyValue
	
	if (xorCandy == 0):
		return sumCandy - leastValuableCandy
	else:
		return None

if __name__ == "__main__":

	if(len(sys.argv) != 3):
		print("Usage: %s inputfile outputfile" % sys.argv[0], file=sys.stderr)
		sys.exit(1)
		
	inputFile = open(sys.argv[1])
	outputFile = open(sys.argv[2], "w")
	
	numTestCases = int(inputFile.readline())
	
	for i in range(1, numTestCases+1):
		numberOfCandies = int(inputFile.readline())
		testCaseString = inputFile.readline()
		testCaseList = testCaseString.split()
		
		if (numberOfCandies != len(testCaseList)):
			print ("Case #%d: Test case mismatch" % i, file=sys.stderr)
		
		seanCandies = calcSeanValue(testCaseList)
		if (seanCandies):
			outputFile.write("Case #%d: %d\n" % (i, seanCandies))
		else:
			outputFile.write("Case #%d: NO\n" % i)
		
	inputFile.close();
	outputFile.close();
		