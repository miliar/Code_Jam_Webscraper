#!/usr/bin/env python

FILE_NAME_BASE = 'B-small-1'
NUM_PROCESSES = 8

def parse(inp):
	rows, cols, baseMass = (int(x) for x in inp.readline().split())
	sheet = []
	for _ in xrange(rows):
		line = tuple(int(x) for x in inp.readline().strip())
		assert len(line) == cols
		sheet.append(line)
	return rows, cols, sheet

def solve(rows, cols, sheet):

	def possible(size):
		for y0 in xrange(rows - size + 1):
			for x0 in xrange(cols - size + 1):
				xs = 0
				ys = 0
				for yi in xrange(size):
					yo = -size + 1 + 2 * yi
					for xi in xrange(size):
						if not ((xi == 0 or xi == size -1) and (yi == 0 or yi == size - 1)):
							xo = -size + 1 + 2 * xi
							m = sheet[y0 + yi][x0 + xi]
							xs += xo * m
							ys += yo * m
				#print size, x0, y0, xs, ys
				if xs == 0 and ys == 0:
					return True
		return False

	size = 3
	maxSize = min(rows, cols)
	largestPossible = None
	for size in xrange(3, maxSize + 1):
		if possible(size):
			largestPossible = size
	
	return 'IMPOSSIBLE' if largestPossible is None else '%s' % largestPossible

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
