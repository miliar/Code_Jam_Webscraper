#!/usr/bin/env python

from string import split, join, strip
from sys import argv, stdin, exit
from math import hypot
from copy import copy
from getopt import getopt
from misc import *
import os.path
import psyco
psyco.full()



def solve(case):
	(P, K, L) = map(int, split(case[0]))
	LFREQ = map(int, split(case[1]))
	KMAP = [None] * L
	
	key_map = {}

	freq_set = kinds(LFREQ)
	freq_set.sort()
	freq_set.reverse()

	p_curr = 1
	k_curr = 1

	for f in freq_set:
		for i in range(L):
			if (LFREQ[i] == f):
#				assert(not (p_curr > P))
#				print LFREQ[i]
#				print 'pc', p_curr, 'kc', k_curr
				KMAP[i] = p_curr
				if (k_curr < K):
					k_curr = k_curr + 1
				else:
					k_curr = 1
					p_curr = p_curr + 1

#	print 'P', P, 'K', K, 'L', L
#	print 'lfreq', LFREQ
#	print 'kmap',KMAP

	r = []
	for i in range(L):
		r.append(KMAP[i] * LFREQ[i])

	return str(sum(r))








def main():
	(max_cases, specific_case) = args(argv)

	cases = int(get_line())

	if (max_cases):
		cases = max_cases

	for c in range(1, cases+1):
		cd = []
		
		LINES_PER_CASE = 2

		for de_nada in range(LINES_PER_CASE):
			cd.append(get_line())
			
		if (specific_case):
			if (c != specific_case):
				continue
			else:
				print cd

		sol = 'Case #' + str(c) + ": " + solve(cd)

		put_line(sol)		
		
		print sol


def get_line():
	global file_in
	return strip(file_in.readline())


def put_line(line):
	global file_out
	if (file_out):
		file_out.write(line + '\n')
	
	
def args(arg_v):
	global file_in
	global file_out

	go = getopt(argv[1:], 'i:o:c:m:')
	
	file_in = None
	file_out = None
	max_cases = None
	specific_case = None
	
	for o in go[0]:
		if (o[0] == '-i'):
			file_in = open(o[1])
		elif (o[0] == '-o'):
			#assert(not os.path.isfile(o[1]))
			file_out = open(o[1], 'w')
		elif (o[0] == '-c'):
			specific_case = int(o[1])
		elif (o[0] == '-m'):
			max_cases = int(o[1])

	assert(file_in)
	
	return (max_cases, specific_case)


main()


