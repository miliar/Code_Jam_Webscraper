#!/usr/bin/env python

from string import split, join, strip
from sys import argv, stdin, exit
from math import hypot
from copy import copy
from getopt import getopt
import os.path
import psyco
psyco.full()



def solve(case):
	(A, B, P) = map(int, split(case[0]))

	R = range(A, B+1)
	RI = range(len(R))
	
	for p in pairs(len(R)):
		if (share_prime(R[p[0]], R[p[1]], P)):
			s0 = RI[ p[0] ]
			s1 = RI[ p[1] ]
		
			for i in range( len(R) ):
				if (RI[i] == s0):
					RI[i] = s1
	
	sets = []
	for si in RI:
		if (si not in sets):
			sets.append(si)

	return str(len(sets))



def primes(n):
	no = n
	p = []
	while (n > 1):
		for i in range(2, n+1):
			if (n % i == 0):
				n = n / i
				p.append(i)

	if (len(p) == 1):
		return [no]

	p2 = []
	
	for i in p:
		p2 = p2 + primes(i)

	p2.sort()	
	return p2

def share_prime(i, j, P):
	ip = primes(i)
	jp = primes(j)

	ipok = []
	
	for p in ip:
		if (p >= P):
			ipok.append(p)
	
	for p in ipok:
		if (p in jp):
			return True
	
	return False

def pairs(N):
	for i in range(N):
		for j in range(i+1, N):
			yield [i,j]





def main():
	(max_cases, specific_case) = args(argv)

	cases = int(get_line())

	if (max_cases):
		cases = max_cases

	for c in range(1, cases+1):
		cd = []
		
		LINES_PER_CASE = 1

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
		

def cmplen(s1, s2):
	if (len(s1) < len(s2)):
		return -1
	elif (len(s1) == len(s2)):
		return 0
	else:
		return 1

	
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


