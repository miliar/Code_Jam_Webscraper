#!/usr/bin/env python

import sys

def solve():
	numEngines = int(sys.stdin.readline())
	engines = []
	for _ in range(numEngines):
		engine = sys.stdin.readline()
		engines.append(engine)

	numQueries = int(sys.stdin.readline())
	queries = []
	for _ in range(numQueries):
		query = sys.stdin.readline()
		queries.append(query)

	remainingEngines = set(engines)
	switches = 0
	for query in queries:
		remainingEngines.discard(query)
		if not remainingEngines:
			remainingEngines = set(engines)
			remainingEngines.discard(query)
			switches += 1

	return switches

cases = int(sys.stdin.readline())
for case in range(cases):
	print 'Case #%d: %s' % (case + 1, solve())
