#! /usr/bin/python

import sys

def readCase():
	line = sys.stdin.readline()
	nengines = int(line.strip())
	ne = 0
	while ne < nengines:
		line = sys.stdin.readline()
		ne += 1
	line = sys.stdin.readline()
	nqueries = int(line.strip())
	nq = 0
	queries = list()	
	while nq < nqueries:
		queries.append(sys.stdin.readline().strip())
		nq += 1
	return nengines, queries

def solveCase(ne, queries):
	s = set()
	nswitch = 0
	for q in queries:
		if q not in s:
			if len(s) == ne - 1:
				nswitch += 1
				s.clear()
			s.add(q)
	return nswitch

if __name__ == "__main__":
	line = sys.stdin.readline()
	ncases = int(line.strip())
	nc = 0
	while nc < ncases:
		ne, queries = readCase()
		nswitch = solveCase(ne, queries)
		print "Case #%d: %d" % (nc + 1, nswitch)
		nc += 1
