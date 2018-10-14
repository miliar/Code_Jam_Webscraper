#!/usr/bin/env python

from collections import defaultdict

FILE_NAME_BASE = 'B-large'
NUM_PROCESSES = 0

def parse(inp):
	i = iter(inp.readline().split())
	numProductions = int(i.next())
	productions = [ i.next() for _ in xrange(numProductions) ]
	numOpposed = int(i.next())
	opposed = [ i.next() for _ in xrange(numOpposed) ]
	numInvoked = int(i.next())
	invoked = i.next()
	assert len(invoked) == numInvoked
	assert len(list(i)) == 0
	return productions, opposed, invoked

def solve(productions, opposed, invoked):
	productionMap = {}
	for base1, base2, nonbase in productions:
		productionMap[base1 + base2] = nonbase
		productionMap[base2 + base1] = nonbase
	#print 'prod', productionMap
	
	opposedMap = defaultdict(set)
	for base1, base2 in opposed:
		opposedMap[base1].add(base2)
		opposedMap[base2].add(base1)
	#print 'opp', opposedMap
	
	elem = []
	for base in invoked:
		elem.append(base)
		if len(elem) < 2:
			produced = None
		else:
			produced = productionMap.get(elem[-2] + elem[-1])
		if produced is not None:
			elem = elem[ : -2] + [ produced ]
		else:
			opposites = opposedMap.get(base)
			if opposites is not None and opposites & set(elem[ : -1]):
				elem = []
				
	return '[%s]' % (', '.join(elem))

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
