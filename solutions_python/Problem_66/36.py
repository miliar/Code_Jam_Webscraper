import pdb
import sys
import re
import time
from collections import namedtuple
from itertools import *
from copy import copy, deepcopy

taskname = 'B'
input = None

class Best_dict(dict):
	def __setitem__(self, k, v):
		if k not in self or self[k] > v:
			dict.__setitem__(self, k, v)

def readstr():
	return next(input).strip()

def readintlist():
	lst = map(int, readstr().split())
	return lst

def readint():
	lst = readintlist()
	assert len(lst) == 1
	return lst[0]

def fuse_dicts(d1, d2):
	new = Best_dict()
	for k1, v1 in d1.iteritems():
		for k2, v2 in d2.iteritems():
			k = min(k1, k2)
			v = v1 + v2
			new[k] = v
	return new

def select(d1, d2, price):
	fused = fuse_dicts(d1, d2)
	best = Best_dict()
	for k, v in fused.iteritems():
		best[k] = v + price
		if k > 0:
			best[k - 1] = v
	return best

def grouper(n, iterable, fillvalue=None):
	"grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
	args = [iter(iterable)] * n
	return izip_longest(fillvalue=fillvalue, *args)

def solvecase():
	p = readint()
	constraints = readintlist()
	assert len(constraints) == 2 ** p
	prices = []
	for i in range(p):
		round_prices = readintlist()
		assert len(round_prices) == 2 ** (p - i - 1)
		prices.append(round_prices)
		
	constraints = [{k : 0} for k in constraints]
	
	for round_prices in prices:
		cnew = []
		for (a, b), p in izip(grouper(2, constraints), round_prices):
#			print a, b, p
			cnew.append(select(a, b, p))
		constraints = cnew
	assert len(constraints) == 1
	#print constraints
	return min(constraints[0].itervalues())

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
