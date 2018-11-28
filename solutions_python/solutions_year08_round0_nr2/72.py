#!/usr/bin/env python

from string import split, join, strip
from sys import argv, stdin, exit
from math import hypot
from copy import copy

LINES_PER_CASE = None


def solve(case):
	H = 60
	TAT = int(case[0])
	(NA, NB) = map(int, split(case[1]))

	A = 0
	B = 1

	DEP = [[], []]
	
	for t in case[2:2+NA]:
		(d, a) = split(t)
		(h, m) = split(d, ':')
		d = int(h) * H + int(m)
		(h, m) = split(a, ':')
		a = int(h) * H + int(m)
		DEP[A].append( [d, a] )

	DEP[A].sort()

	for t in case[2+NA:]:
		(d, a) = split(t)
		(h, m) = split(d, ':')
		d = int(h) * H + int(m)
		(h, m) = split(a, ':')
		a = int(h) * H + int(m)
		DEP[B].append( [d, a] )
	
	DEP[B].sort()
	
	NEEDED = [0, 0]
	AVAIL = [[], []]
	
	while (DEP[A] or DEP[B]):
		ab = None
		
		if (DEP[A] and DEP[B]):
			if (DEP[A][0] < DEP[B][0]):
				ab = A
			else:
				ab = B
		elif (DEP[A]):
			ab = A
		else:
			ab = B
		
		train = DEP[ab][0]
		DEP[ab].remove(train)
		
		train_dep_time = train[0]
		train_arr_time = train[1]
		
		if (AVAIL[ab] and AVAIL[ab][0] <= train_dep_time):
			AVAIL[ab].remove( AVAIL[ab][0] )
		else:
			NEEDED[ab] = NEEDED[ab] + 1

		AVAIL[1-ab].append( train_arr_time + TAT )
		AVAIL[1-ab].sort()
		
	return '%i %i' % (NEEDED[A], NEEDED[B])


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
		cd = []
		cd.append(strip(f.readline()))
		cd.append(strip(f.readline()))
		
		(a, b) = map(int, split(cd[-1]))
		
		for de_nada in range(a+b):
			cd.append(strip(f.readline()))
			
		if (specific_case):
			if (c != specific_case):
				continue
			else:
				print cd

		print 'Case #' + str(c) + ": " + solve(cd)

main()
