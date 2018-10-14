#!/usr/bin/env python
from sys import stdin

T = int(stdin.readline())
	
def analyse(total, threshold):
	"""
	Ret 0 if not possible
	Ret 1 if possible if surprise
	Ret 2 if possible without surprise
	"""
	div = total/3
	rem = total%3
	
	if rem == 0:
		if threshold <= div : return 2  
		if threshold > div+1: return 0
		# threshold == div+1
		if div == 0: return 0
		return 1
	
	if rem == 1:
		if threshold <= div+1 : return 2
		if threshold > div+1: return 0
		
	if rem == 2:
		if threshold <= div+1: return 2
		if threshold > div+2 : return 0
		#threshold == div+2
		if div >= 9: return 0
		return 1
	
	
	
for i in xrange(T):
	
	line = map(int, stdin.readline().split(" "))
	N = line[0] # nb of dansers
	S = line[1] # nb suprise
	p = line[2] # limit
	totals = line[3:]
	
	alwaysok = 0
	ifsurprise = 0
	
	
	for total in totals:
		
		res = analyse(total, p)
		if res == 2: alwaysok += 1
		if res == 1: ifsurprise += 1
	
	result = alwaysok + min(ifsurprise, S)

	print "Case #%d: %d" % (i+1, result)
