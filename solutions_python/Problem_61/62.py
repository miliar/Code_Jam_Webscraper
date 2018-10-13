import pdb
import sys
import re
import time
from collections import namedtuple
from itertools import *
from copy import copy, deepcopy

taskname = 'C'
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

def memoized(f):
	d = {}
	def wrapper(*args):
		if args in d: return d[args]
		res = f(*args)
		d[args] = res
		return res
	return wrapper

MOD = 100003

sys.setrecursionlimit(10000)

@memoized
def cnk(n, k):
	if n == k or k == 0: return 1
	assert n > k and k > 0
	return (cnk(n - 1, k - 1) + cnk(n - 1, k)) % MOD 

@memoized
def f(n, pos):
	if pos == 1: return 1
	total = 0
	for p1 in range(1, pos):
		d0 = n - pos - 1
		d1 = pos - p1 - 1
		if d1 > d0: continue
		w1 = f(pos, p1)
		w2 = cnk(d0, d1)
		total = (total + w1 * w2) % MOD
	return total

def solvecase():
	n = readint()
	total = 0
	for pos in range(1, n):
		total = (total + f(n, pos)) % MOD 
	return total

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
