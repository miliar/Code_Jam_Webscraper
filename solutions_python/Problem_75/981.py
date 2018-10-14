#!/usr/bin/env python

#import numpy as np
import sys, os
import math
import itertools


def get_in_groups(k, n):
	for x in range(0, len(k), n):
		yield k[x:x+n]
		

def preprocess_combinations(Q, qstr):
	result = {}
	for c1, c2, c3 in get_in_groups(qstr, 3):
		result[(c1,c2)] = c3
	return result
		
		
def preprocess_oppositions(Q, qstr):
	result = []
	for g in get_in_groups(qstr, 2):
		result.append(g)
	return result
		

def solve(line):
	C = int(line.pop(0))
	Cs = {}
	for c in range(C):
		c1, c2, c3 = line.pop(0)
		Cs[(c1,c2)] = c3
#	Cs = preprocess_combinations(C, line.pop(0)) if C > 0 else {}
	
	D = int(line.pop(0))
#	Ds = preprocess_oppositions(D, line.pop(0)) if D > 0 else {}
	Ds = []
	for d in range(D):
		Ds.append(line.pop(0))
		
	
	N = int(line.pop(0))
	Ns = line.pop(0)
	
	output = []
	for n in Ns:
		if len(output) == 0:
			output.append(n)
			continue

		end = (output[-1],n) 		
		
		if end in Cs:
			output.pop()
			output.append(Cs[end])
			continue
		elif tuple(reversed(end)) in Cs:
			output.pop()
			output.append(Cs[tuple(reversed(end))])
			continue
			
		hits = itertools.ifilter(lambda x: n in x, Ds)
		clear = False
		for hit in hits:
			other = hit[int(not hit.index(n))]
			if other in output:
				clear = True
				break
		if clear:
			output = []
			continue
		
		output.append(n)
		
	return output
		
		

def main():
	rl = sys.stdin.readline
	T = int(rl())
				
	for t in xrange(T):
		print "Case #%i: %s" % (t+1, str(solve(rl().split())).replace("'", ""))
					
			
main()