import pdb
import sys
import re
import time
from collections import namedtuple
from itertools import *
from copy import copy, deepcopy

taskname = 'A'
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

#def simulate(n, k):
#	snappers = [False] * n

def solvecase():
	n, k = readints()
	k %= 2 ** n
	k += 1
	res = k == 1 << n
	write('ON' if res else 'OFF')

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
