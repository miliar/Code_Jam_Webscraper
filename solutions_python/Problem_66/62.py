#!/usr/bin/python

import sys

def readInput():
	file = open(sys.argv[1])

	testCaseCount = int(file.readline().rstrip())

	testCases = []
	for i in xrange(testCaseCount):
		P = int(file.readline().rstrip())
		M = [int(x) for x in file.readline().rstrip().split()]
		prices = [[int(x) for x in file.readline().rstrip().split()] for i in xrange(P)]

		testCases.append((P, M, prices))
	
	return testCases

def solve((P, M, prices)):
	bought = set()

	for team in xrange(len(M)):
		for visit in xrange(P - M[team]):
			match = team >> P - visit
			bought.add((P - visit - 1, match))
	
	price = 0

	for ticket in bought:
		price += prices[ticket[0]][ticket[1]]

	return price

def notDone(P, M):
	for m in M:
		if m < P:
			return True

	return False

testCases = readInput()

testCaseNr = 1
for testCase in testCases:
	print 'Case #%d: %s' % (testCaseNr, solve(testCase))
	testCaseNr += 1
