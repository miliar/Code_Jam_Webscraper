#!/usr/bin/env python

import sys

def solve(engines, queries):
	num_sw = 0
	if (len(queries) == 0):
		return 0
	avail = set(engines)
	for q in queries:
		if (q in avail):
			avail.remove(q)
		if (len(avail) == 0):
			num_sw += 1
			avail = set(engines)
			avail.remove(q)
	return num_sw

if (len(sys.argv) < 2):
	print "usage: su.py <infile>"
	sys.exit(1)

f = open(sys.argv[1], 'r')

case = 1
state = 0
for line in f:
	if (state == 0):
		state = 1
	elif (state == 1):
		num_engines = (int) (line.strip())
		engines = []
		state = 2
	elif (state == 2):
		engines.append(line.strip())
		if (num_engines == len(engines)):
			state = 3
	elif (state == 3):
		num_queries = (int) (line.strip())
		queries = []
		if (num_queries == 0):
			res = solve(engines, queries)
			print "Case #%d: %d" % (case, res)
			case += 1
			state = 1
		else:
			state = 4
	elif (state == 4):
		queries.append(line.strip())
		if (num_queries == len(queries)):
			res = solve(engines, queries)
			print "Case #%d: %d" % (case, res)
			case += 1
			state = 1


