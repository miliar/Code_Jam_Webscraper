#!/usr/bin/env python

FILE_NAME_BASE = 'A-large'
NUM_PROCESSES = 4

from collections import defaultdict

def emptyTree():
	return defaultdict(emptyTree)

def insert(tree, path):
	assert path[0] == ''
	for name in path[1 : ]:
		tree = tree[name]

def parse(inp):
	numExisting, numWanted = (int(x) for x in inp.readline().split())
	existingTree = emptyTree()
	for _ in xrange(numExisting):
		path = inp.readline().rstrip().split('/')
		insert(existingTree, path)
	wantedTree = emptyTree()
	for _ in xrange(numWanted):
		path = inp.readline().rstrip().split('/')
		insert(wantedTree, path)
	return existingTree, wantedTree

def countMissing(existingTree, wantedTree):
	total = 0
	for path in wantedTree.iterkeys():
		if path not in existingTree:
			total += 1
		total += countMissing(existingTree[path], wantedTree[path])
	return total

def solve(existingTree, wantedTree):
	return countMissing(existingTree, wantedTree)

if __name__ == '__main__':
	inp = open(FILE_NAME_BASE + '.in', 'r')
	numCases = int(inp.readline())
	if NUM_PROCESSES == 0:
		results = [
			solve(*parse(inp))
			for _ in range(numCases)
			]
	else:
		from multiprocessing import Pool
		pool = Pool(NUM_PROCESSES)
		results = [
			pool.apply_async(solve, parse(inp))
			for _ in range(numCases)
			]
	inp.close()
	out = open(FILE_NAME_BASE + '.out', 'w')
	for case, result in enumerate(results):
		value = result if NUM_PROCESSES == 0 else result.get()
		out.write('Case #%d: %s\n' % (case + 1, value))
		out.flush()
	out.close()
