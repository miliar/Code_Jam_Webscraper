#!/usr/bin/python

import sys

def readInput():
	file = open(sys.argv[1])

	testCaseCount = int(file.readline().rstrip())

	testCases = [int(file.readline().rstrip()) for line in xrange(testCaseCount)]
	
	return testCases

solutions = {}

def solve(n):
	if n not in solutions:
		# slow naive solution
		solution = recurse(n, 2, []) % 100003
		solutions[n] = solution

	return solutions[n]

def recurse(n, i, s):
	if i > n:
		return check(n, s)
	return recurse(n, i + 1, s + [i]) + recurse(n, i + 1, s)

def check(n, s):
	while n != 1:
		if n not in s:
			return 0
		n = s.index(n) + 1

	return 1

testCases = readInput()

testCaseNr = 1
for testCase in testCases:
	print 'Case #%d: %s' % (testCaseNr, solve(testCase))
	testCaseNr += 1
