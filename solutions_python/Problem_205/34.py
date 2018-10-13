#!/usr/bin/env python

FILE_NAME_BASE = 'C-small-attempt1'
NUM_PROCESSES = 4
MEM_LIMIT_GB = 1.5 # per worker process
RECURSION_LIMIT = 1000

def parse(inp):
	drHP, drAtk, knHP, knAtk, buff, debuff = (int(x) for x in inp.readline().split())
	return drHP, drAtk, knHP, knAtk, buff, debuff

def solve(drHP, drAtk, knHP, knAtk, buff, debuff):
	drFullHP = drHP
	states = set()
	states.add((drHP, drAtk, knHP, knAtk))
	turn = 1
	while states:
		# Dragon's move.
		newStates = set()
		for drHP, drAtk, knHP, knAtk in states:
			# Attack.
			if knHP <= drAtk:
				# Knight loses.
				return turn
			else:
				newStates.add((drHP, drAtk, knHP - drAtk, knAtk))
			# Buff.
			newStates.add((drHP, drAtk + buff, knHP, knAtk))
			# Cure.
			if knAtk >= drHP:
				newStates.add((drFullHP, drAtk, knHP, knAtk))
			# Debuff.
			if knAtk > 0 and debuff > 0:
				newStates.add((drHP, drAtk, knHP, max(knAtk - debuff, 0)))
		# Knight's move.
		newStates2 = set()
		for drHP, drAtk, knHP, knAtk in newStates:
			drHP -= knAtk
			if drHP > 0:
				newStates2.add((drHP, drAtk, knHP, knAtk))
		if newStates2 == states:
			# Stalemate.
			break
		states = newStates2
		turn += 1
	return 'IMPOSSIBLE'

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
