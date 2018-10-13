#!/usr/bin/env python

import sys

def calculate_switches(engines, queries):

	switch = 0

	no_of_engines = len(engines)
	#print '%s' % no_of_engines
	cur_engines = []

	for q in queries:

		if q in engines: #check if query is the name of a search engine
			if q not in cur_engines:
				cur_engines.append(q)
				if len(cur_engines) >= no_of_engines:
					cur_engines = [q]
					#print 'Yipee!'
					switch = switch + 1
	
	return switch

if __name__ == "__main__":
	
	inp = open(sys.argv[1])
	op = open(sys.argv[2], 'w')

	cases = int(inp.readline()[:-1])
	
	for i in range(1, cases + 1):
		engines = []
		queries = []
		
		s = int(inp.readline()[:-1])
		for j in range(1, s + 1):
			engines.append(inp.readline()[:-1])
			
		q = int(inp.readline()[:-1])
		for k in range(1, q+1):
			queries.append(inp.readline()[:-1])
			
		op.write('Case #%s: %s\n' % (i, calculate_switches(engines, queries)))
	
	inp.close()
	op.close()
