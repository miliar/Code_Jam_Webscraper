#!/usr/bin/env python

#FILE_NAME_BASE = 'C-example'
#FILE_NAME_BASE = 'C-small-1-attempt0'
#FILE_NAME_BASE = 'C-small-2-attempt0'
FILE_NAME_BASE = 'C-large'
NUM_PROCESSES = 0
MEM_LIMIT_GB = 1.5 # per worker process
RECURSION_LIMIT = 1000

from collections import defaultdict

def parse(inp):
	numStalls, numPeople = (int(x) for x in inp.readline().split())
	return numStalls, numPeople

def solve(numStalls, numPeople):
	freq = defaultdict(int)
	freq[numStalls] = 1
	numOccupied = 0
	while True:
		empty = max(freq.iterkeys())
		fe = freq[empty]
		assert fe != 0, empty
		ls = (empty - 1) / 2
		rs = empty - ls - 1
		numOccupied += fe
		if numOccupied >= numPeople:
			return '%d %d' % (rs, ls)
		del freq[empty]
		freq[ls] += fe
		freq[rs] += fe

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
