#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys

rl = sys.stdin.readline

t = int(rl())

def gcd(u, v) :
	nGcd = u
	tmp1 = v
	tmp2 = 0
	
	while tmp1 > 0 :
		tmp2 = nGcd % tmp1
		nGcd = tmp1
		tmp1 = tmp2
		
	return nGcd
	
	
for c in range(0, t) :
	cur = map(int, rl().split())
	loop = cur[0]
	cur.pop(0)
		
	diff = []
	for i in range(0, loop) :		
		for j in range(0, loop) :
			if i == j: continue
			diff.append(abs(cur[i]-cur[j]))
			
			
	diff = list(set(diff))
	
	nGcd = 0
	lGcd = []
	if len(diff) == 1 :
		nGcd = diff[0]
	else :
		for i in range(0, len(diff)) :
			for j in range(0, len(diff)) :
				if i == j: continue
				lGcd.append(gcd(diff[i], diff[j]))
				
		lGcd = list(set(lGcd))
		nGcd = lGcd[0]
		
	trg = min(cur)
	
	while trg > 0 :
		trg = trg - nGcd
		
	out = 'Case #%d: ' % (c+1)
	out = out + str(abs(trg))
	print out
			
	
			
			
			
		

	

