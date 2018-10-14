#!/usr/bin/env python

FILE_NAME_BASE = 'A-large'
NUM_PROCESSES = 0

def parse(inp):
	parts = inp.readline().split()
	numPushes = int(parts[0])
	assert numPushes * 2 + 1 == len(parts)
	which = parts[1 : : 2]
	where = [ int(x) for x in parts[2 : : 2] ]
	assert len(which) == len(where)
	return which, where

def solve(which, where):
	now = 0
	pos = { 'B': (1, now), 'O': (1, now) }
	for who, to in zip(which, where):
		(fr, t) = pos[who]
		t += abs(fr - to)
		t = max(now, t) + 1
		pos[who] = (to, t)
		now = t
	return now

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
