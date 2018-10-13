#!/usr/bin/env python

FILE_NAME_BASE = 'B-large'
NUM_PROCESSES = 4
MEM_LIMIT_GB = 1.5 # per worker process
RECURSION_LIMIT = 1000

def parse(inp):
	rounds, prizes = (int(x) for x in inp.readline().split())
	return rounds, prizes

def search(low, high, test):
	'''Binary search: [low..high) is the range to search; function "test"
	takes a single value from that interval and returns a truth value.
	The function must be ascending: (test(x) and y >= x) => test(y).
	Returns smallest argument in the interval for which the function is true,
	or "high" if the function is false for the entire interval.
	'''
	while low < high:
		mid = (low + high - 1) / 2
		if test(mid):
			if mid == low:
				return low # found
			high = mid + 1
		else:
			low = mid + 1
	return high # not found

def solve(rounds, prizes):

	#def winLucky(team, rnd, record):
		#numWorse = ?
		#return numWorse > 0

	#def winUnlucky(team, rnd, record):
		#numBetter = ?
		
		#if rnd == 0:
			#numBetter = team
		
		
		#return numBetter == 0

	#def play(team, winFunc):
		#record = 0
		#for rnd in xrange(rounds):
			#record = (record << 1) | int(winFunc(team, rnd, record))
		#return record

	#def worstRank(team):
		#return play(team, winUnlucky)

	#def bestRank(team):
		#return play(team, winLucky)

	def worstRank(team):
		numBetter = team
		record = 0
		for rnd in xrange(rounds):
			win = numBetter == 0
			record = (record << 1) | int(not win)
			if not win:
				numBetter = (numBetter - 1) / 2
		return record

	def bestRank(team):
		numWorse = (1 << rounds) - 1 - team
		record = 0
		for rnd in xrange(rounds):
			win = numWorse != 0
			record = (record << 1) | int(not win)
			if win:
				numWorse = (numWorse - 1) / 2
		return record

	worstCertainPrize = \
		search(0, 1 << rounds, lambda t: worstRank(t) >= prizes) - 1
	worstMaybePrize = \
		search(0, 1 << rounds, lambda t: bestRank(t) >= prizes) - 1

	assert 0 <= worstCertainPrize < (1 << rounds), worstCertainPrize
	assert 0 <= worstMaybePrize < (1 << rounds), worstMaybePrize

	return '%d %d' % (worstCertainPrize, worstMaybePrize)

def main():
	import sys
	sys.setrecursionlimit(RECURSION_LIMIT)

	import resource
	soft, hard = resource.getrlimit(resource.RLIMIT_AS)
	resource.setrlimit(resource.RLIMIT_AS, (MEM_LIMIT_GB * 1024 ** 3, hard))

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

if __name__ == '__main__':
	main()
