#!/usr/bin/python
import sys

infile = open(sys.argv[1], 'r')

numCases = int(infile.readline())
caseNum = 0

for case in range(numCases):
	caseNum += 1
	numVals = int(infile.readline())
	nums = [int(i) for i in infile.readline().split()]
	
	numOff = 0
	for i in range(len(nums)):
		if i != nums[i]-1:
			numOff += 1
	
	print "Case #%s: %6f" % (caseNum, numOff)
