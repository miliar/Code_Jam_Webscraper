#!/usr/bin/env python

FILE_NAME_BASE = 'A-large-0'
NUM_PROCESSES = 0

def parse(inp):
	numTeams, = (int(x) for x in inp.readline().split())
	numWon = [ 0 ] * numTeams
	numPlayed = [ 0 ] * numTeams
	opponents = [ [] for _ in xrange(numTeams) ]
	results = []
	for team in xrange(numTeams):
		line = inp.readline().strip()
		lineRes = []
		assert len(line) == numTeams
		for opp, resCh in enumerate(line):
			if resCh == '.':
				res = None
			else:
				numPlayed[team] += 1
				opponents[team].append(opp)
				res = int(resCh)
				numWon[team] += res
			lineRes.append(res)
		results.append(lineRes)
	return results, numWon, numPlayed, opponents

def solve(results, numWon, numPlayed, opponents):
	numTeams = len(numWon)
	
	wp = [ None ] * numTeams
	for team in xrange(numTeams):
		wp[team] = numWon[team] / float(numPlayed[team])
	
	owp = [ None ] * numTeams
	for team in xrange(numTeams):
		owp[team] = sum(
			(numWon[opp] - results[opp][team]) / float(numPlayed[opp] - 1)
			for opp in opponents[team]
			) / numPlayed[team]

	oowp = [ None ] * numTeams
	for team in xrange(numTeams):
		oowp[team] = sum(
			owp[opp]
			for opp in opponents[team]
			) / numPlayed[team]
	
	return '\n' + '\n'.join(
		'%0.12f' % (0.25 * (wp[team] + 2 * owp[team] + oowp[team]))
		for team in xrange(numTeams)
		)

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
