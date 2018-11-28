#!/usr/bin/python

import sys

f = open(sys.argv[1], 'r')

num_of_cases = int(f.readline())
case_counter = 1

def check_row(lawn, v, r, m):
	for i in range(m):
		if lawn[r][i] > v:
			return True 

	return False

def check_column(lawn, v, c, n):
	for i in range(n):
		if lawn[i][c] > v:
			return True 
			
	return False

def is_possible(lawn, n, m):
	for r in range(n):
		for c in range(m):
			if (check_row(lawn, lawn[r][c], r, m) ) and (check_column(lawn, lawn[r][c], c, n)):
				return False 

	return True

while case_counter <= num_of_cases:
	[ n, m ] = [ int(x) for x in f.readline().strip().split(' ') ]

	lines = [ f.readline() for i in range(n) ]
	lawn = [] 
	#lawn.append([-1]*(m+1))
	digits = set()
	for line in lines:	
		#lawn_line = [ -1 ]
		#lawn_line.extend( [ int(x) for x in line.strip().split(' ') ] )
		#lawn_line.append(-1)
		lawn_line = [ int(x) for x in line.strip().split(' ') ]
		lawn.append(lawn_line)

	#lawn.append([-1]*(m+1))
	#for ll in lawn:
	#	print ll 

	result = 'YES' if is_possible(lawn, n, m ) else 'NO'

	print "Case #%i: %s" % ( case_counter, result)
 
	case_counter += 1
