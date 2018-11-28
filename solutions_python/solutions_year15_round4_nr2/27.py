#!/usr/bin/env python

FILE_NAME_BASE = 'B-small-attempt0'
NUM_PROCESSES = 0
MEM_LIMIT_GB = 1.5 # per worker process
RECURSION_LIMIT = 1000

def parse(inp):
	parts = inp.readline().split()
	numTaps = int(parts[0])
	targetVolume, targetTemp = (float(x) for x in parts[1:])
	taps = tuple(
		tuple(float(x) for x in inp.readline().split())
		for _ in xrange(numTaps)
		)
	return taps, targetVolume, targetTemp

def solve(taps, targetVolume, targetTemp):
	if max(temp for rate, temp in taps) < targetTemp:
		return 'IMPOSSIBLE'
	if min(temp for rate, temp in taps) > targetTemp:
		return 'IMPOSSIBLE'

	if len(taps) == 1:
		rate, temp = taps[0]
		return targetVolume /rate

	if len(taps) == 2:
		(rate0, temp0), (rate1, temp1) = taps
		if temp0 == temp1:
			return targetVolume / (rate0 + rate1)

		# part0 * temp0 + (1 - part0) * temp1 == targetTemp
		# part0 * (temp0 - temp1) == targetTemp - temp1
		part0 = (targetTemp - temp1) / (temp0 - temp1)
		part1 = 1 - part0

		time0 = (part0 * targetVolume) / rate0
		time1 = (part1 * targetVolume) / rate1

		return max(time0, time1)

	return '--- not implemented ---'

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
