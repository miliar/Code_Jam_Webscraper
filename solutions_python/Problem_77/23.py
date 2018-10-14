#!/usr/bin/env python

import random
from collections import defaultdict

	#[1] => 0.000
	#[2,1] => n
	# hold none
	#		n = 1 + (1/2) * 0 + (1/2) * n
	#		n/2 = 1
	#		n = 2
	#
	#[2,3,1] = n
	# hold none
	#		n = 1 + 3/6 * gorosort(2) + 2/6 * n
	#		n =	1 + 3/6 * 2 + n*2/6
	#		4/6*n = 2
	#		n = 12/4 = 3
	# hold down one
	#		n = 2 + 2 = 4
	#
	#[2,3,4,1] = n			4 loop
	# hold down none
	#		n = 1 + (9/24) * 0 + 6/24 * gorosort(2) + 8/24 * gorosort(3) + 9/24 * n
	#		n = 1 + 12/24 + 1 + 9/24 *n
	#		15/24*n = 2.5
	#		n = 4
	#
	#[2,1,4,3]			2 loop + 2 loop = 2 + 2 = 4
	#
	#[2,3,4,5,1] = n
	#		n = 1 + 10/120 * g(2) + 20/120 * g(3) + 45/120 * g(4) + 44/120 * n
	#		76/120 * n = 1 + 1/6 + 1/2 + 3/2
	#		76/120 * n = 19/6
	#		n = 5
	#

def solve(line):
	values = map(int, (line.strip()).split())
	assert sorted(values) == range(1,len(values)+1)
	
	correct = 0
	for index, value in enumerate(values,1):
		if index == value:
			correct += 1
	
	return len(values) - correct


def solveFile(Filename):
	inFile = open(Filename, "r")
	outFile = open(Filename[:-2]+"out", "w")
	tests = int(inFile.readline())
	for i, line in enumerate(inFile.readlines()[1::2],1):
		outFile.write("Case #{0}: {1}\n".format(i, solve(line)))

solveFile("example.in")
solveFile("D-small-attempt0.in")
solveFile("D-large.in")

