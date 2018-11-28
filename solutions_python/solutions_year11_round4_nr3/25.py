# -*- coding: utf-8 -*-


from __future__ import division
from math import log as ln
from collections import defaultdict as dd



ps = [2]
def primes():
	global ps
	for n in ps: yield n
	while True:
		found = False
		while not found:
			n += 1
			comp = False
			for d in ps:
				if d*d>n:
					break
				if n%d==0:
					comp = True
					break
			found = not comp
		yield n
		ps.append(n)
		



T = int(raw_input())

for t in xrange(1,T+1):
	
	N = int(raw_input())
	
	mint = 0
	if N==1: mint = 1
	maxt = 1	# make 1 come first
	
	for p in primes():
		if p>N: break
		exp = int(ln(N)/ln(p))
		if p**(exp+1) <= N:
			exp += 1
		mint += 1
		maxt += exp
	
	print 'Case #{x}: {y}'.format(x=t, y=maxt-mint)




























































