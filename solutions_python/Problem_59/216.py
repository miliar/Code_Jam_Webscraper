#!/usr/bin/python

import sys

def readInput():
	file = open(sys.argv[1])

	testCaseCount = int(file.readline().rstrip())
	testCases = []

	for testCase in xrange(testCaseCount):
		n, m = [int(x) for x in file.readline().rstrip().split()]

		existingDirs = [file.readline().rstrip() for line in xrange(n)]
		wantedDirs = [file.readline().rstrip() for line in xrange(m)]

		testCases.append((existingDirs, wantedDirs))

	return testCases

class Directory(object):
	def __init__(self):
		self.subdirs = {}

def solve((existingDirs, wantedDirs)):
	root = Directory()

	for path in existingDirs:
		currentDir = root

		for component in path.split('/')[1:]:
			if component not in currentDir.subdirs:
				currentDir.subdirs[component] = Directory()

			currentDir = currentDir.subdirs[component]

	mkdirs = 0

	for path in wantedDirs:
		currentDir = root

		for component in path.split('/')[1:]:
			if component not in currentDir.subdirs:
				currentDir.subdirs[component] = Directory()
				mkdirs += 1

			currentDir = currentDir.subdirs[component]

	return mkdirs

testCases = readInput()

testCaseNr = 1
for testCase in testCases:
	print 'Case #%d: %s' % (testCaseNr, solve(testCase))
	testCaseNr += 1
