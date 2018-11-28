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

def solvecase():
	r, k, n = readintlist()
	groups = readintlist()
	assert n == len(groups)
	positions = [None] * n  
	sum_groups = sum(groups)
	if sum_groups <= k:
		return r * sum_groups
	
	def ride(pos, profit):
		capacity_left = k
		while True:
			capacity_left -= groups[pos]
			if capacity_left < 0: return pos, profit 
			profit += groups[pos]
			pos = (pos + 1) % n
		
	pos = 0
	profit = 0
	cnt = 0
	# calculate cycle
	while r and positions[pos] is None:
		newpos, newprofit = ride(pos, profit)
		positions[pos] = (cnt, profit)
		pos, profit = newpos, newprofit  
		cnt += 1
		r -= 1
	if r:
		# then we must've found a cycle!
		oldcnt, oldprofit = positions[pos]
		cycle_length = cnt - oldcnt
		cycle_profit = profit - oldprofit
		cycles, r = divmod(r, cycle_length)
		profit += cycles * cycle_profit
		# and finish it up
		while r: 
			pos, profit = ride(pos, profit)
			r -= 1
	return profit

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
