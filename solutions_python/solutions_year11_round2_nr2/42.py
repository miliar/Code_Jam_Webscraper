#!/usr/bin/env python

FILE_NAME_BASE = 'B-large-0'
NUM_PROCESSES = 0

from itertools import izip

def parse(inp):
	numPoints, minDist = (int(x) for x in inp.readline().split())
	points = tuple(
		(int(x) for x in inp.readline().split())
		for _ in xrange(numPoints)
		)
	return points, minDist

def solve(points, minDist):
	flatPoints = []
	for x, v in points:
		flatPoints.extend([x] * v)
	flatPoints = sorted(flatPoints)
	#print flatPoints
	
	prePoints = [ (x - i * minDist) * 2 for i, x in enumerate(flatPoints) ]
	
	preMax = []
	m = None
	for x in prePoints:
		preMax.append(m)
		m = max(m, x)
	
	dists = []
	for x, m in izip(prePoints, preMax):
		dists.append(None if m is None else m - x)
	maxDist = max(dists)
	
	t2 = max(0, maxDist)
	return '%1.1f' % (0.25 * t2)

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
