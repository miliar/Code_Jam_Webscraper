#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys

def process(engines, queries):
	data = {}
	
	queries_size = len(queries)
	i = queries_size-1
	
	data = {}
	count = {}
	for engine in engines:
		count[engine] = 0
		
	while i >= 0:
		query = queries[i]
		data[i] = {}
		for engine in engines:
			if engine == query:
				count[engine] = 0
			else:
				count[engine] = count[engine] + 1
			data[i][engine] = count[engine]
		i = i-1

	selectes = -1
	step = 0
	while step < queries_size:
		selectes = selectes + 1
		m = 0
		for engine, engines_count in data[step].items():
			if m < engines_count:
				m = engines_count
		step = step + m
			
	return max(selectes, 0)
	
def main():
	f = open('A-large.in')
	
	cases = int(f.readline().strip())
	for i in range(cases):
		total_engines = int(f.readline().strip())
		engines = []
		for e in range(total_engines):
			engines.append(f.readline().strip())
		
		total_queries = int(f.readline().strip())
		queries = []
		for q in range(total_queries):
			queries.append(f.readline().strip())
		
		result = process(engines, queries)
		print "Case #" + str(i+1) + ": " + str(result)
	f.close()

if __name__ == '__main__':
	sys.exit(main())


