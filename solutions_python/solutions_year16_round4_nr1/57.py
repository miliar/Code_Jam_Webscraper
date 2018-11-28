#!/usr/bin/env python

FILE_NAME_BASE = 'A-small-attempt0'
NUM_PROCESSES = 0
MEM_LIMIT_GB = 1.5 # per worker process
RECURSION_LIMIT = 1000

def parse(inp):
	n, r, p, s = (int(x) for x in inp.readline().split())
	return n, r, p, s

def deadlock(lineup):
	while len(lineup) > 1:
		winners = []
		for a, b in zip(lineup[::2], lineup[1::2]):
			if a == b:
				return True
			if max(a, b) == 'S' and min(a, b) == 'R':
				winners.append('R')
			elif max(a, b) == 'R' and min(a, b) == 'P':
				winners.append('P')
			elif max(a, b) == 'S' and min(a, b) == 'P':
				winners.append('S')
			else:
				assert False, (a, b)
		lineup = winners
	return False

def solve(n, r, p, s):
	participants = 1 << n

	def rec(lineup, r, p, s):
		if len(lineup) == participants:
			if not deadlock(lineup):
				yield ''.join(lineup)
		if r > 0:
			lineup.append('R')
			for found in rec(lineup, r - 1, p, s):
				yield found
			del lineup[-1]
		if p > 0:
			lineup.append('P')
			for found in rec(lineup, r, p - 1, s):
				yield found
			del lineup[-1]
		if s > 0:
			lineup.append('S')
			for found in rec(lineup, r, p, s - 1):
				yield found 
			del lineup[-1]

	lineups = sorted(rec([], r, p, s))
	return lineups[0] if len(lineups) > 0 else 'IMPOSSIBLE'

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
