#!/usr/bin/env python

FILE_NAME_BASE = 'A-large'
NUM_PROCESSES = 4
MEM_LIMIT_GB = 1.5 # per worker process
RECURSION_LIMIT = 1000

def parse(inp):
	rows, cols = (int(x) for x in inp.readline().split())
	grid = tuple(inp.readline().strip() for _ in xrange(rows))
	assert all(len(row) == cols for row in grid)
	return grid,

def solve(grid):
	rows = len(grid)
	cols = len(grid[0])

	arrows = tuple(
		(x, y)
		for x in xrange(cols)
		for y in xrange(rows)
		if grid[y][x] != '.'
		)

	dirs = '^>v<'
	dirDelta = ((0, -1), (1, 0), (0, 1), (-1, 0))

	changed = 0
	for x, y in arrows:
		redirected = []
		for dx, dy in dirDelta:
			wx, wy = x + dx, y + dy
			while 0 <= wx < cols and 0 <= wy < rows and grid[wy][wx] == '.':
				wx += dx
				wy += dy
			redirected.append(0 <= wx < cols and 0 <= wy < rows)
		startDir = dirs.index(grid[y][x])
		if not redirected[startDir]:
			if any(redirected):
				changed += 1
			else:
				return 'IMPOSSIBLE'

	return changed

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
