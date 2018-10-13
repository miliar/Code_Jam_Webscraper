#!/usr/bin/env python

FILE_NAME_BASE = 'C-small-attempt0'
NUM_PROCESSES = 0

def isPure(n, subset):
	try:
		while True:
			n = subset.index(n) + 1
	except ValueError:
		return n == 1

def precalc(n):
	numPure = 0
	for bits in xrange(1 << (n - 1)):
		subset = []
		for i in xrange(2, n + 1):
			if (bits >> (i - 2)) & 1:
				subset.append(i)
		if isPure(n, subset):
			numPure += 1
	return numPure

#numPure = tuple(precalc(n) for n in xrange(2, 25 + 1))
numPure = (1, 2, 3, 5, 8, 14, 24, 43, 77, 140, 256, 472, 874, 1628, 3045, 5719, 10780, 20388, 38674, 73562, 140268, 268066, 513350, 984911)

def parse(inp):
	n, = (int(x) for x in inp.readline().split())
	return n,

def solve(n):
	return numPure[n - 2] % 100003

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
