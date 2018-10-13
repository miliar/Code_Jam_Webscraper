#!/usr/bin/env python

FILE_NAME_BASE = 'A-large'
NUM_PROCESSES = 0
MEM_LIMIT_GB = 1.5 # per worker process
RECURSION_LIMIT = 1000

def parse(inp):
	numAvailable, numOrdered = (int(x) for x in inp.readline().split())
	pancakes = tuple(
		tuple(int(x) for x in inp.readline().split())
		for _ in xrange(numAvailable)
		)
	return pancakes, numOrdered

from math import pi

def solve(pancakes, numOrdered):
	pancakes = sorted(
		(r, h * 2 * pi * r)
		for r, h in pancakes
		)
	best = 0
	for bottomIdx, bottom in enumerate(pancakes):
		bottomRad = bottom[0]
		base = pi * bottomRad ** 2
		candidates = []
		for candIdx, candidate in enumerate(pancakes):
			if candIdx != bottomIdx and candidate[0] <= bottomRad:
				candidates.append(candidate[1])
		sides = [bottom[1]] + sorted(candidates, reverse=True)[:numOrdered - 1]
		area = base + sum(sides)
		best = max(best, area)
	return best

def main():
	import sys
	sys.setrecursionlimit(RECURSION_LIMIT)

	import resource
	soft, hard = resource.getrlimit(resource.RLIMIT_AS)
	resource.setrlimit(resource.RLIMIT_AS, (MEM_LIMIT_GB * 1024 ** 3, hard))

	with open(FILE_NAME_BASE + '.in', 'r') as inp:
		numCases = int(inp.readline())
		inputs = [parse(inp) for _ in xrange(numCases)]

	if NUM_PROCESSES == 0:
		runners = [lambda inp=inp: apply(solve, inp) for inp in inputs]
	else:
		from multiprocessing import Pool
		from signal import SIGINT, SIG_IGN, signal
		pool = Pool(NUM_PROCESSES, signal, (SIGINT, SIG_IGN))
		runners = [pool.apply_async(solve, inp).get for inp in inputs]
		pool.close()

	caseFmt = '%' + str(len(str(numCases))) + 'd'
	progressFmt = '[%s/%s] %%s\n' % (caseFmt, caseFmt)
	with open(FILE_NAME_BASE + '.out', 'w') as out:
		for case, runner in enumerate(runners, 1):
			result = runner()
			out.write('Case #%d: %s\n' % (case, result))
			out.flush()
			sys.stderr.write(progressFmt % (case, numCases, result))

if __name__ == '__main__':
	main()
