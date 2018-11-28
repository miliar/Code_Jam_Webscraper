#!/usr/bin/env python

FILE_NAME_BASE = 'C-large'
NUM_PROCESSES = 4

def parse(inp):
	runs, size, numGroups = (int(x) for x in inp.readline().split())
	groups = [int(x) for x in inp.readline().split()]
	assert numGroups == len(groups)
	return runs, size, groups

def solve(runs, size, groups):
	# Never put non-existant people in the coaster.
	size = min(size, sum(groups))

	numGroups = len(groups)
	past = [ None ] * numGroups

	pos = 0
	money = 0
	run = 0
	while run < runs:
		if past[pos] is None:
			past[pos] = (run, money)
		else:
			pastRun, pastMoney = past[pos]
			past = [ None ] * numGroups
			period = run - pastRun
			cycles = (runs - run) / period
			if cycles != 0:
				run += cycles * period
				money += cycles * (money - pastMoney)
				continue
		boarded = 0
		while True:
			newBoarded = boarded + groups[pos]
			if newBoarded > size:
				break
			boarded = newBoarded
			pos = (pos + 1) % numGroups
		money += boarded
		run += 1

	return money

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
