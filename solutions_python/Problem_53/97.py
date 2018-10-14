#!/usr/bin/env python

FILE_NAME_BASE = 'A-large'
NUM_PROCESSES = 4

def parse(inp):
	length, snaps = (int(x) for x in inp.readline().split())
	return length, snaps

def solve(length, snaps):
	allOn = (1 << length) - 1
	return 'ON' if (snaps & allOn) == allOn else 'OFF'

if __name__ == '__main__':
	from multiprocessing import Pool
	pool = Pool(NUM_PROCESSES)
	inp = open(FILE_NAME_BASE + '.in', 'r')
	numCases = int(inp.readline())
	results = [
		pool.apply_async(solve, parse(inp))
		for _ in range(numCases)
		]
	inp.close()
	out = open(FILE_NAME_BASE + '.out', 'w')
	for case, result in enumerate(results):
		out.write('Case #%d: %s\n' % (case + 1, result.get()))
		out.flush()
	out.close()
