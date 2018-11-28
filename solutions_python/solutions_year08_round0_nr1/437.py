#!/usr/bin/env python

import sets
import sys

import psyco
psyco.full()


def solve():
	f = open(sys.argv[1])
	N = int(f.readline())
	for n in range(N):
		switches = 0
		search_engines = sets.Set()
		queries = [ ]

		S = int(f.readline())
		for s in range(S):
			search_engines.add(f.readline().strip())

		Q = int(f.readline())
		for q in range(Q):
			queries.append(f.readline().strip())

		remaining_queries = queries

		while True:
			if not remaining_queries or search_engines - sets.Set(remaining_queries):
				break
		
			resn = 0
			for search_engine in search_engines:
				t = 0
				
				for query in remaining_queries:
					if query != search_engine:
						t = t + 1
					else:
						break
	
				if t > resn:
					resn = t
				
			remaining_queries = remaining_queries[resn:]
			switches = switches + 1;	
		
		print("Case #%i: %i" % (n + 1, switches))

solve()