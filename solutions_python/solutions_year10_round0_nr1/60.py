#!/usr/bin/python

import sys

def readInput():
	file = open(sys.argv[1])

	testCaseCount = int(file.readline().rstrip())

	testCases = [[int(x) for x in file.readline().rstrip().split()] for line in xrange(testCaseCount)]
	
	return testCases

def solve((n, k)):
	power = 2 ** n
	if k % power == power - 1:
		return 'ON'
	else:
		return 'OFF'

testCases = readInput()

testCaseNr = 1
for testCase in testCases:
	print 'Case #%d: %s' % (testCaseNr, solve(testCase))
	testCaseNr += 1
