#!/usr/bin/python

import sys

def readInput():
	file = open(sys.argv[1])

	testCaseCount = int(file.readline().rstrip())

	testCases = []
	for i in xrange(testCaseCount):
		grid = set()
		
		R = int(file.readline().rstrip())
		for j in xrange(R):
			X1, Y1, X2, Y2 = [int(x) for x in file.readline().rstrip().split()]

			for x in xrange(X1, X2 + 1):
				for y in xrange(Y1, Y2 + 1):
					grid.add((x, y))

		testCases.append(grid)

	return testCases

def solve(grid):
	# north: decreasing Y
	# west: decreasing X
	seconds = 0

	while grid:
		seconds += 1

		newGrid = set()

		for x,y in grid:
			# case: bacterium survives
			if (x-1,y) in grid or (x,y-1) in grid:
				newGrid.add((x, y))

			# case: this north bacterium spawns a new bacterium
			if (x-1,y+1) in grid:
				newGrid.add((x, y+1))

		grid = newGrid

	return seconds

testCases = readInput()

testCaseNr = 1
for testCase in testCases:
	print 'Case #%d: %s' % (testCaseNr, solve(testCase))
	testCaseNr += 1
