#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def other(robot):
	if robot == 'O':
		return 'B'
	elif robot == 'B':
		return 'O'
	else:
		print "Error! Unknown Robot %s" % robot
		return 'O'

def solve(nstep, dat):
	prev = { 'O' : 1, 'B' : 1 }
	moved = { 'O' : 0, 'B' : 0 }
	total_time = 0
	for i in range(nstep):
		robot = dat[2*i]
		btn = int(dat[2*i+1])
		time = max(abs(prev[robot] - btn) - moved[robot], 0) + 1
		
		total_time += time
		prev[robot] = btn
		moved[robot] = 0
		moved[other(robot)] += time
		
	return total_time

def solve_a(infile):
	f = open(infile)
	ntest = int(f.readline())
	for i in range(ntest):
		dat = f.readline().rstrip().split()
		nstep = int(dat.pop(0))
		ans = solve(nstep, dat)
		print "Case #%d: %d" % (i+1, ans)
		
def main():
	if len(sys.argv) > 1:
		solve_a(sys.argv[1])
	else:
		print "no input file."

if __name__ == '__main__':
	main()

