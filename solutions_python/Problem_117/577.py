import copy
import unittest

def readInput(filename):
	'''
	Return a list of test cases
	'''
	f = open(filename)
	numTests = int(f.readline())
	tests = [None] * numTests
	for k in range(numTests):
		(N,M) = [int(x) for x in f.readline().split()]
		lawn = [None] * N
		for i in range(N):
			lawn[i] = [int(x) for x in f.readline().split()]
		tests[k] = lawn
	return tests

def writeOutput(filename, results):
	g = open(filename, 'w')
	for i in range(len(results)):
		g.write("Case #{}: {}\n".format(i+1, results[i]))
	g.close()

def isRowMax(lawn, i, j):
	return lawn[i][j] == max(lawn[i])

def isColumnMax(lawn, i, j):
	for k in range(len(lawn)):
		if lawn[i][j] < lawn[k][j]:
			return False
	return True

def checkPossible(lawn):
	N = len(lawn)
	M = len(lawn[0])

	for i in range(N):
		for j in range(M):
			if not isRowMax(lawn, i, j) and not isColumnMax(lawn, i, j):
				return 'NO'
	return 'YES'

def solveAll(testId):
	lawns = readInput(testId + '.in')
	results = [checkPossible(lawn) for lawn in lawns]
	writeOutput(testId + '.out', results)

def printLawn(lawn):
		for row in lawn:
			print row
		print

def printLawns(testId):
	tests = readInput(testId + '.in')
	for test in tests:
		printLawn(test)

if __name__ == '__main__':
#	printLawns('sample')

#	solveAll('sample')
	solveAll('B-large')

