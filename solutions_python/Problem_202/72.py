#!/usr/bin/env python

#FILE_NAME_BASE = 'D-example'
#FILE_NAME_BASE = 'D-small-attempt1'
FILE_NAME_BASE = 'D-large'
NUM_PROCESSES = 0
MEM_LIMIT_GB = 1.5 # per worker process
RECURSION_LIMIT = 1000

from itertools import ifilter, izip

def parse(inp):
	size, numModels = (int(x) for x in inp.readline().split())
	stage = [['.'] * size for _ in range(size)]
	for _ in range(numModels):
		typ, rowStr, colStr = inp.readline().split()
		assert typ in '+xo', typ
		row = int(rowStr) - 1
		col = int(colStr) - 1
		stage[row][col] = typ
	return stage,

def checkValid(stage):
	size = len(stage)

	# Horizontal.
	for row in xrange(size):
		limitedModels = 0
		for col in xrange(size):
			if stage[row][col] in 'xo':
				limitedModels += 1
		assert limitedModels <= 1

	# Vertical.
	for col in xrange(size):
		limitedModels = 0
		for row in xrange(size):
			if stage[row][col] in 'xo':
				limitedModels += 1
		assert limitedModels <= 1

	# Slash.
	for dia in xrange(size * 2 - 1):
		limitedModels = 0
		for col in xrange(size):
			row = dia - col
			if 0 <= row < size and stage[row][col] in '+o':
				limitedModels += 1
		assert limitedModels <= 1

	# Backslash.
	for dia in xrange(size * 2 - 1):
		limitedModels = 0
		for col in xrange(size):
			row = dia - size + 1 + col
			if 0 <= row < size and stage[row][col] in '+o':
				limitedModels += 1
		assert limitedModels <= 1

def solve(orgStage):
	size = len(orgStage)

	# Deep copy of stage data.
	stage = [list(rowData) for rowData in orgStage]
	checkValid(stage)

	# Determine which rows and columns have restricted models in them.
	rowTaken = [False] * size
	colTaken = [False] * size
	for row, rowData in enumerate(stage):
		for col, typ in enumerate(rowData):
			if typ == 'x' or typ == 'o':
				assert not rowTaken[row]
				rowTaken[row] = True
				assert not colTaken[col]
				colTaken[col] = True

	# Place x/o models where possible.
	freeRows = ifilter(lambda row: not rowTaken[row], xrange(size))
	freeCols = ifilter(lambda col: not colTaken[col], xrange(size))
	for row, col in izip(freeRows, freeCols):
		stage[row][col] = {'.' : 'x', '+': 'o'}[stage[row][col]]
	checkValid(stage)

	# Determine which diagonals have restricted models in them.
	diaPTaken = [False] * (size * 2 - 1)
	diaMTaken = [False] * (size * 2 - 1)
	for row, rowData in enumerate(stage):
		for col, typ in enumerate(rowData):
			if typ == '+' or typ == 'o':
				assert not diaPTaken[row + col]
				diaPTaken[row + col] = True
				assert not diaMTaken[row - col + size - 1]
				diaMTaken[row - col + size - 1] = True

	# Iterate through diagonals from short to long.
	def diaWalk():
		for i in xrange(size):
			yield i
			if i != size - 1:
				yield size * 2 - 2 - i
	assert sorted(diaWalk()) == range(size * 2 - 1)

	# Place +/o models where possible.
	freeDiaPs = ifilter(lambda dia: not diaPTaken[dia], diaWalk())
	freeDiaMs = ifilter(lambda dia: not diaMTaken[dia], diaWalk())
	freeDiaMs = list(freeDiaMs)
	for diaP in freeDiaPs:
		for i, diaM in enumerate(freeDiaMs):
			col2 = diaP - diaM + size - 1
			if col2 & 1 == 0:
				col = col2 / 2
				row = diaP - col
				if 0 <= row < size and 0 <= col < size:
					stage[row][col] = {'.' : '+', 'x': 'o'}[stage[row][col]]
					del freeDiaMs[i]
					break
	checkValid(stage)

	# Calculate style points.
	points = 0
	for rowData in stage:
		for typ in rowData:
			i = '.+xo'.index(typ)
			points += (i & 1) + (i >> 1)

	# Collect changes.
	changes = []
	for row, rowData in enumerate(stage):
		for col, typ in enumerate(rowData):
			if typ != orgStage[row][col]:
				changes.append((typ, row + 1, col + 1))

	# Format output.
	output = ['%d %d' % (points, len(changes))]
	for change in changes:
		output.append('%s %d %d' % change)
	return '\n'.join(output)

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
