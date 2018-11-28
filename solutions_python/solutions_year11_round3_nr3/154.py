#!/usr/bin/env python

import operator
import math
from pprint import pprint
from fractions import gcd

log = False

def solve(L, H, freqs):
	if log:
		print 'Notes from %d to %d' % (L, H)
		print 'Freqs ', freqs
	
	max_freqs = max(freqs)
	min_freqs = min(freqs)
	
	for i in range(L, H+1):		
		t = True
		for j in freqs:
			if not harm(i, j):
				t = False
		if t:
			return str(i)
	
	return 'NO'
	
def harm(f1, f2):
	if f1 % f2 ==0:
		return True
	elif f2 % f1 ==0:
		return True
	else:
		return False
						
if __name__ == '__main__':    
	with open('C-small-0.in') as f:
		lines = f.readlines()

	problems = []

	line_num = 0
	
	num_problems = int(lines[line_num])# T:1 to 40
	line_num += 1
	
	for i in range(num_problems):
		N, L, H = map(int, lines[line_num].split()) #N: 1 to 10000, 0 < L < H < 10e16
		line_num += 1
		
		freqs = map(int, lines[line_num].split()) #N
		line_num += 1

		problems.append((L, H, freqs))

	if log:
		pprint(problems)

	for problem_num, problem in enumerate(problems):
		if log:
			print '###'
			print problem
		
		answer = solve(*problem)
		
		
		print 'Case #%s: %s' % (problem_num+1, answer)




