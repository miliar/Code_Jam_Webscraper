#!/usr/bin/env python

FILE_NAME_BASE = 'A-large-0'
NUM_PROCESSES = 0

def parse(inp):
	maxToday, winToday, winEver = (int(x) for x in inp.readline().split())
	return maxToday, winToday, winEver

def gcd(a, b):
	'''Returns the greatest common divisor of a and b.
	'''
	while a != 0:
		a, b = b % a, a
	return b

def lcm(a, b):
	'''Returns the least common multiple of a and b.
	'''
	d = gcd(a, b)
	return (a / d) * b

def solve(maxToday, percWinToday, percWinEver):
	# percWinEver = 100 * numWinEver / numPlayedEver
	# percWinToday = 100 * numWinToday / numPlayedToday
	# percWinEver is integer
	# percWinToday is integer
	# 0 <= numWinToday <= numWinEver
	# 0 <= numWinToday <= maxToday
	# 1 <= numPlayedToday <= numPlayedEver
	# numPlayedEver - numWinEver >= numPlayedToday - numWinToday
	#   numPlayedEver - numPlayedToday >= numWinEver - numWinToday
	#
	# percWin * numPlayed = 100 * numWin = k * lcm = k * gcd * percWin * 100
	# k > 0 because we played at least one game today (and therefore ever)
	#
	# numPlayed = k * 100 / gcd
	
	stepToday = 100 / gcd(percWinToday, 100)
	possible = (
		stepToday <= maxToday
		and (percWinEver > 0 or percWinToday == 0)
		and (percWinEver < 100 or percWinToday == 100)
		)
	return 'Possible' if possible else 'Broken'

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
