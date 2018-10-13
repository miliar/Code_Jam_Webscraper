#!/usr/bin/env python

FILE_NAME_BASE = 'B-large'
NUM_PROCESSES = 4
MEM_LIMIT_GB = 1.5 # per worker process
RECURSION_LIMIT = 1000

from collections import defaultdict

def parse(inp):
	numIngr, numPacks = (int(x) for x in inp.readline().split())
	recipe = tuple(int(x) for x in inp.readline().split())
	assert len(recipe) == numIngr
	packs = tuple(
		tuple(int(x) for x in inp.readline().split())
		for _ in xrange(numIngr)
		)
	assert all(len(packIngr) == numPacks for packIngr in packs)
	return recipe, packs

def solve(recipe, packs):
	ingrServings = []
	for perServing, contents in zip(recipe, packs):
		packServings = []
		for grams in contents:
			low = (grams * 10) / (11 * perServing)
			if low * 11 * perServing < grams * 10:
				low += 1
			assert low * 11 * perServing >= grams * 10

			high = (grams * 10) / (9 * perServing)
			assert high * 9 * perServing <= grams * 10

			if low <= high:
				packServings.append((low, high))
		ingrServings.append(packServings)

	events = defaultdict(list)
	for ingr, packServings in enumerate(ingrServings):
		for low, high in packServings:
			events[low].append((ingr, 1))
			events[high + 1].append((ingr, -1))

	numIngr = len(recipe)
	kits = 0
	numPackagesInRange = [0] * numIngr
	numPackagesUsed = [0] * numIngr
	for servings in sorted(events.iterkeys()):
		for ingr, delta in events[servings]:
			numPackagesInRange[ingr] += delta
			if delta < 0:
				numPackagesUsed[ingr] = max(0, numPackagesUsed[ingr] + delta)
		addKits = min(
			numPackagesInRange[ingr] - numPackagesUsed[ingr]
			for ingr in xrange(numIngr)
			)
		for ingr in xrange(numIngr):
			numPackagesUsed[ingr] += addKits
		kits += addKits
	for ingr in xrange(numIngr):
		assert numPackagesInRange[ingr] == 0, ingr

	return kits

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
