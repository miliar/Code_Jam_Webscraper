#!/usr/bin/env python

FILE_NAME_BASE = 'B-large'
NUM_PROCESSES = 4

from itertools import izip

def parse(inp):
	numChicks, numArrive, barnDist, endTime = \
		(int(x) for x in inp.readline().split())
	startPos = tuple(int(x) for x in inp.readline().split())
	assert len(startPos) == numChicks
	speed = tuple(int(x) for x in inp.readline().split())
	assert len(speed) == numChicks
	return numArrive, barnDist, endTime, startPos, speed

def solve(numArrive, barnDist, endTime, startPos, speed):
	# Fast chicks are the ones that will make it to the barn if they are not
	# held up by slow chicks.
	fast = tuple(
		x + v * endTime >= barnDist
		for x, v in izip(startPos, speed)
		)
	#print numArrive, fast
	target = numArrive
	numSlow = 0
	swaps = 0
	for isFast in reversed(fast):
		if isFast:
			swaps += numSlow
			target -= 1
			if target == 0:
				#print swaps
				return swaps
		else:
			numSlow += 1
	else:
		return 0 if numArrive == 0 else 'IMPOSSIBLE'

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
