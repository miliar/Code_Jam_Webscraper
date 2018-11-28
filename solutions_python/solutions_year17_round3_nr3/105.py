#!/usr/bin/env python

FILE_NAME_BASE = 'C-small-1-attempt0'
NUM_PROCESSES = 0
MEM_LIMIT_GB = 1.5 # per worker process
RECURSION_LIMIT = 1000

def parse(inp):
	numCores, numSuccess = (int(x) for x in inp.readline().split())
	units, = (float(x) for x in inp.readline().split())
	rates = tuple(float(x) for x in inp.readline().split())
	assert len(rates) == numCores
	return numSuccess, units, rates

def solve(success, units, rates):
	if success != len(rates):
		return 'not-implemented'

	rates = sorted(rates)
	idx = 0
	minRate = rates[0]
	while idx < len(rates) and rates[idx] == minRate:
		idx += 1
	while minRate < 1.0:
		nextRate = rates[idx] if idx < len(rates) else 1.0
		trainRate = minRate + units / idx
		if trainRate < nextRate:
			# Out of training units.
			minRate = trainRate
			break
		units -= (nextRate - minRate) * idx
		minRate = nextRate
		while idx < len(rates) and rates[idx] == minRate:
			idx += 1

	return reduce(lambda x, y: x * y, rates[idx:], minRate ** idx)

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
