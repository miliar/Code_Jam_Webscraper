#!/usr/bin/env python

import sys

la = {}; lb = {}
for p in range(1,11):
	la[p] = 3*p - 4
	lb[p] = 3*p - 2
la[1] = 1

def solve(N, S, p, scores):
	global la, lb
	a = 0; b = 0
	if p == 0: return N
	for scr in scores:
		if scr >= lb[p]: 
			b = b + 1; 
		elif scr >= la[p]: 
			a = a + 1
	return b + min(a, S)
		

def main(infile):
	n = int(infile.readline())
	for i in range(n):
		cmd = infile.readline().split()
		N = int(cmd.pop(0))
		S = int(cmd.pop(0))
		p = int(cmd.pop(0))
		scores = [int(x) for x in cmd]
		print 'Case #%s: %s' % (i+1, solve(N, S, p, scores))

main(sys.stdin)
