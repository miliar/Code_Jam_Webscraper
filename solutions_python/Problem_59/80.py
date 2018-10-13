import pdb
import sys
import re
import time
from collections import namedtuple
from itertools import *
from copy import copy, deepcopy

taskname = 'A'
input = None

def readstr():
	return next(input).strip()

def readintlist():
	lst = map(int, readstr().split())
	return lst

def readint():
	lst = readintlist()
	assert len(lst) == 1
	return lst[0]


def addpath(root, path):
	path = path.split('/')[1:]
	count = 0
	for dir in path:
		if dir in root:
			root = root[dir]
		else:
			new = {}
			root[dir] = new
			root = new
			count += 1
	return count	

def solvecase():
	n, m = readintlist()
	root = {}
	count = 0
	for _ in range(n):
		addpath(root, readstr())
	for _ in range(m):
		count += addpath(root, readstr())
	return count

def solve(suffix):
	global input
	tstart = time.clock()
	input = open(taskname + '-' + suffix + '.in', 'r')
	output = open(taskname + '-' + suffix + '.out', 'w')
	casecount = readint()
	
	for case in range(1, casecount + 1):
		s = solvecase()
		s = "Case #%d: %s" % (case, str(s)) 
		print >>output, s
		print s 
		
	input.close()
	output.close()
	print '%s solved in %.3f' % (suffix, time.clock() - tstart)
			
if __name__ == '__main__':
	solve('small')
	solve('large')
