#!/usr/bin/env python

FILE_NAME_BASE = 'C-small-attempt0'
NUM_PROCESSES = 0
MEM_LIMIT_GB = 1.5 # per worker process
RECURSION_LIMIT = 1000

def parse(inp):
	numCities, numDeliveries = (int(x) for x in inp.readline().split())
	horses = tuple(
		# (endurance, speed)
		tuple(int(x) for x in inp.readline().split())
		for _ in xrange(numCities)
		)
	routes = tuple(
		tuple(int(x) for x in inp.readline().split())
		for _ in xrange(numCities)
		)
	deliveries = tuple(
		# (start, end)
		tuple(int(x) - 1 for x in inp.readline().split())
		for _ in xrange(numDeliveries)
		)
	return horses, routes, deliveries

def solve(horses, routes, deliveries):
	numCities = len(routes)

	if len(deliveries) != 1 or deliveries[0] != (0, numCities - 1):
		return '-non-linear-'

	state = [(0, 0, 0)]
	curCity = 0
	while True:
		fastest = min(time for left, speed, time in state)
		nextCity = curCity + 1
		if nextCity == numCities:
			return fastest
		dist = routes[curCity][nextCity]
		assert dist > 0, dist

		# Add this city's horse to options.
		state.append(horses[curCity] + (fastest,))

		# Try all possible horses.
		newState = []
		for left, speed, time in state:
			if left >= dist:
				newState.append((left - dist, speed, time + dist / float(speed)))
		state = newState
		curCity = nextCity

	return (horses, routes, deliveries)

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
