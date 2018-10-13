#!/usr/bin/python

import sys

def readInput():
	file = open(sys.argv[1])

	testCaseCount = int(file.readline().rstrip())

	testCases = [[int(x) for x in file.readline().rstrip().split()[1:]] for line in xrange(testCaseCount)]
	
	return testCases

def gcd(a, b):
	while b != 0:
		(a, b) = (b, a % b)

	return a

def solve(testCase):
	smallest = min(testCase)
	numsMinusSmallest = [x - smallest for x in testCase if x - smallest != 0]

	gcdSoFar = numsMinusSmallest[0]
	for num in numsMinusSmallest[1:]:
		gcdSoFar = gcd(gcdSoFar, num)

	return (gcdSoFar - testCase[0]) % gcdSoFar

testCases = readInput()

testCaseNr = 1
for testCase in testCases:
	print 'Case #%d: %s' % (testCaseNr, solve(testCase))
	testCaseNr += 1
