#!/usr/bin/env python

from string import split, join, strip
from sys import argv, stdin, exit
from math import hypot
from copy import copy

LINES_PER_CASE = None


def solve(case):
	E = case[0]
	Q = case[1]
	QL = len(Q)
	CONSUMED = 0
	
	if (CONSUMED == QL):
		return '0'

#	print E
#	print Q	

	eng = copy(E)
	switches = -1
	
	while (CONSUMED != QL):
		switches = switches + 1
		CONSUMED = how_far(Q, eng, CONSUMED)
#		print eng
		i = E.index(eng[0])
		eng = E[0:i] + E[i+1:]
#		print eng
#		print CONSUMED



	return str(switches)



def how_far(q, e, start):
	ql = len(q)
	for i in range(start, ql):
		if (len(e) == 1):
			if (q[i] == e[0]):
				return i
		else:
			if (q[i] in e):
				e.remove(q[i])
	
	return ql




def main():
	global LINES_PER_CASE
	
	f = open(argv[1])

	cases = int(f.readline())

	specific_case = None
	if (len(argv) > 2):
		if (argv[2][0] == '.'):
			specific_case = int(argv[2][1:])
		else:
			max_cases = int(argv[2])
			if (max_cases < cases):
				cases = max_cases

	for c in range(1, cases+1):
		e = []
		q = []
		
		for de_nada in range(int( strip(f.readline()) )):
			e.append(strip(f.readline()))
		for de_nada in range(int( strip(f.readline()) )):
			q.append(strip(f.readline()))
		
		cd = [e, q]
		
		if (specific_case):
			if (c != specific_case):
				continue
			else:
				print cd

		print 'Case #' + str(c) + ": " + solve(cd)

main()
