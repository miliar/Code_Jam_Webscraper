#!/usr/bin/env python

FILE_NAME_BASE = 'C-large'
NUM_PROCESSES = 0

def parse(inp):
	numCandies, = (int(x) for x in inp.readline().split())
	candyValues = [ int(x) for x in inp.readline().split() ]
	assert len(candyValues) == numCandies
	return candyValues,

def solve(candyValues):
	xorValue = reduce(int.__xor__, candyValues, 0)
	if xorValue == 0:
		return sum(candyValues) - min(candyValues)
	else:
		return 'NO'

if __name__ == '__main__':
	inp = open(FILE_NAME_BASE + '.in.txt', 'r')
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
	out = open(FILE_NAME_BASE + '.out.txt', 'w')
	for case, result in enumerate(results):
		value = result if NUM_PROCESSES == 0 else result.get()
		out.write('Case #%d: %s\n' % (case + 1, value))
		out.flush()
	out.close()
