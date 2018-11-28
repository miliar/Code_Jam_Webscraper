import pdb
import sys
import re
import time
from collections import namedtuple
from itertools import *
from copy import copy, deepcopy

taskname = 'B'
input = None
output = None
case = None

def readstr():
	return next(input).strip()

def readintlist():
	lst = map(int, readstr().split())
	return lst

def readints():
	lst = readintlist()
	return lst[0] if len(lst) == 1 else lst

def write(s):
	s = "Case #%d: %s" % (case, str(s))
	print >>output, s
	print s 

def gcd(a, b):
	if a < b: a, b = b, a
	while b:
		a, b = b, a % b
	return a
		
#for i in range(10):
#	for j in range(10):
#		print '%2d %2d: %d' % (i, j, gcd(i, j))

def solvecase():
	numbers = readintlist()
	assert numbers[0] == len(numbers) - 1
	numbers.pop(0)
	numbers.sort()
	base = numbers.pop()
	numbers = [base - i for i in numbers]
	g = reduce(gcd, numbers)
	elapsed = base % g
	left = (g - elapsed) % g
	write(left)

def solve(suffix):
	global input, output, taskname, case
	tstart = time.clock()
	input = open(taskname + '-' + suffix + '.in', 'r')
	output = open(taskname + '-' + suffix + '.out', 'w')
	casecount = readints()
	for case in range(1, casecount + 1):
		solvecase()
	input.close()
	output.close()
	print '%s solved in %.3f' % (suffix, time.clock() - tstart)

			
if __name__ == '__main__':
	solve('small')
	solve('large')
