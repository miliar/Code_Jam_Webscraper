import copy
import unittest
import time
import math

class Chest:
	def __init__(self, keyType, keys):
		self.keyType = keyType
		self.keys = keys
		self.keySet = set(keys)

	def __repr__(self):
		return "keyType: {}, keys: {}".format(self.keyType, self.keys)

class State:
	def __init__(self, keyCount, opened):
		self.keyCount = keyCount[:]
		self.opened = opened[:]

class SearchState:
	def __init__(self, state, path):
		self.state = state
		self.path = path

def readInput(filename):
	'''
	Return a list of test cases
	'''
	f = open(filename)
	numTests = int(f.readline())
	tests = [None] * numTests
	for i in range(numTests):
		(numKeys, numChests) = [int(x) for x in f.readline().split()]
		keys = [int(x) for x in f.readline().split()]

		chests = [None] * (numChests + 1)
		maxKeyType = max(keys)

		for n in range(1, numChests+1):
			chestInfo = [int(x) for x in f.readline().split()]
			chestKeyType = chestInfo[0]
			numKeysInChest = chestInfo[1]
			keysInChest = chestInfo[2:]

			chests[n] = Chest(chestKeyType, keysInChest)

			if len(keysInChest) > 0:
				maxKeyType = max(maxKeyType, max(keysInChest))

		keyCount = [0] * (maxKeyType+1)
		for key in keys:
			keyCount[key] += 1

		tests[i] = (keyCount, chests)

	return tests

def writeOutput(filename, results):
	g = open(filename, 'w')
	for i in range(len(results)):
		g.write("Case #{}: {}\n".format(i+1, results[i]))
	g.close()

def isSolved(searchState):
	for x in searchState.state.opened:
		if not x:
			return False
	return True

def highPriority(chest):
	if chest.keyType in chest.keySet:
		return True
	else:
		return False

def feasible(state, chests):
	totalKeyCount = state.keyCount[:]
	totalKeyNeeded = [0] * len(totalKeyCount)
	for i in range(1, len(chests)):
		if not state.opened[i]:
			totalKeyNeeded[chests[i].keyType] += 1
			for key in chests[i].keys:
				totalKeyCount[key] += 1

#	print totalKeyCount
#	print totalKeyNeeded

	for i in range(1, len(totalKeyCount)):
		if totalKeyCount[i] < totalKeyNeeded[i]:
			return False

	for i in range(1, len(chests)):
		if not state.opened[i]:
			keyType = chests[i].keyType
			hiddenCount = chests[i].keys.count(keyType)
			totalCount = totalKeyCount[keyType]
			if hiddenCount == totalCount:
				return False

	return True

def formatResult(path):
	return ' '.join([str(i) for i in path])

def solve(problem):
	(keyCount, chests) = problem

	maxKeyType = len(keyCount) - 1
	numChests = len(chests) - 1

	startState = State(keyCount, [True] + [False] * numChests)

	fringe = [SearchState(startState, [])]

	while len(fringe) > 0:
		searchState = fringe.pop()
		if isSolved(searchState):
			return formatResult(searchState.path)

		state = searchState.state
		path = searchState.path

		if not feasible(state, chests):
			continue

#		highPriorities = []
#		lowPriorities = []
		for i in range(numChests, 0, -1):
			if not state.opened[i] and state.keyCount[chests[i].keyType] > 0:
				newState = State(state.keyCount, state.opened)
				newState.opened[i] = True
				newState.keyCount[chests[i].keyType] -= 1
				for key in chests[i].keys:
					newState.keyCount[key] += 1
				newPath = path + [i]
				newSearchState = SearchState(newState, newPath)
				fringe.append(newSearchState)
#				if highPriority(chests[i]):
#					highPriorities.append(newSearchState)
#				else:
#					lowPriorities.append(newSearchState)
#		fringe.extend(lowPriorities)
#		fringe.extend(highPriorities)

	return "IMPOSSIBLE"

def solveAll(testId):
	tests = readInput(testId + '.in')
	results = [None] * len(tests)
	for i in range(len(tests)):
		print("TestCase #{}".format(i+1))
		printProblem(tests[i])
		result = solve(tests[i])
		print("result = {}\n".format(result))
		results[i] = result

#	results = [solve(test) for test in tests]
	writeOutput(testId + '.out', results)

def printProblem(problem):
	(keyCount, chests) = problem
	print("keyCount:")
	for key in range(1, len(keyCount)):
		print("{}: {}".format(key, keyCount[key]))

	print("chests:")
	for i in range(1, len(chests)):
		print("{}: {}".format(i, chests[i]))

def printProblems(testId):
	tests = readInput(testId + '.in')
	for test in tests:
		printProblem(test)
		print

if __name__ == '__main__':
#	printProblems('sample')

#	solveAll('sample')
#	solveAll('sample2')
	solveAll('D-small-attempt2')

