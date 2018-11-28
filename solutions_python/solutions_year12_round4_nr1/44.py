#!/usr/bin/env python

FILE_NAME_BASE = 'A-large'
NUM_PROCESSES = 4

import sys
sys.setrecursionlimit(20000)

def parse(inp):
	numVines = int(inp.readline())
	vines = [
		tuple(int(x) for x in inp.readline().split())
		for _ in xrange(numVines)
		]
	dest = int(inp.readline())
	vines.append((dest, 0))
	return tuple(vines),

def solve(vines):
	numVines = len(vines)

	tried = [0] * numVines
	def rec(i, l):
		if i == numVines - 1:
			return True
		else:
			longest = tried[i]
			if l < longest:
				return False
			tried[i] = l
			di, li = vines[i]
			for j in xrange(i + 1, numVines):
				dj, lj = vines[j]
				if di + l >= dj:
					if rec(j, min(lj, dj - di)):
						return True
				else:
					break
			return False

	return 'YES' if rec(0, vines[0][0]) else 'NO'

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
