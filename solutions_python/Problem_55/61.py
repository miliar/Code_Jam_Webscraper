#!/usr/bin/python

import sys

def readInput():
	file = open(sys.argv[1])

	testCaseCount = int(file.readline().rstrip())

	testCases = []

	for i in xrange(testCaseCount):
		R, k, N = (int(x) for x in file.readline().rstrip().split())
		groups = [int(x) for x in file.readline().rstrip().split()]
		testCases.append((R, k, N, groups))
	
	return testCases

def solve(testCase):
	R, k, N, groups = testCase

	euros = 0

	for i in xrange(R):
		nextGroup = groups[0]
		remainingSeats = k
		seatedGroups = []

		while nextGroup <= remainingSeats:
			remainingSeats -= nextGroup
			del groups[0]
			seatedGroups.append(nextGroup)

			if len(groups) == 0:
				break

			nextGroup = groups[0]

		groups += seatedGroups

		euros += k - remainingSeats

	return euros

testCases = readInput()

testCaseNr = 1
for testCase in testCases:
	print 'Case #%d: %s' % (testCaseNr, solve(testCase))
	testCaseNr += 1
