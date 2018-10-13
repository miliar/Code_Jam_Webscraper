#import sys
#import numpy as np
#import random as rnd
#from math import log, pi

def strSig(s):
	prevCh = s[0]
	sign = [prevCh]
	nrep = [1]
	for ch in s[1:]:
		if ch!=prevCh:
			sign.append(ch)
			nrep.append(1)
		else:
			nrep[-1]+= 1
		prevCh = ch
	return (sign, nrep) 

def solve_case(lst):
	(sign, nrep) = strSig(lst[0])
	
	nreps = [[0 for i in xrange(len(lst))] for j in xrange(len(nrep))]
	for i in xrange(len(nrep)):
		nreps[i][0] = nrep[i]
	
	lstIdx = 1
	for entry in lst[1:]:
		(sign1, nrep) = strSig(entry)
		if sign1!=sign:
			return 'Fegla Won'
		else:
			for i in xrange(len(nrep)):
				nreps[i][lstIdx] = nrep[i]
		lstIdx+=1
	
	# If we get this far, then Fegla didn't win
	tot = 0
	for nr in nreps:		
		nr.sort()
		c = [nr[0]]
		for i in nr[1:]:
			c.append(c[-1]+i)
		E = 1000*c[-1]
		for v in xrange(len(c)):
			val = nr[v]
			cE = 0
			if v>0:
				cE += (v*val-c[v-1])
			if v<len(c)-1:
				cE += (c[-1]-c[v]-(len(c)-v-1)*val)
			if(cE<E):
				E = cE
		tot += E
		
	return tot
			

def solve(in_name, out_name):
	fin = open(in_name, 'r');
	L = [x.strip() for x in fin.readlines()]
	fin.close()
	
	T = int(L[0])
	
	res = []
	idx = 1
	for casenr in xrange(1, T+1):
		N = int(L[idx])
		idx+=1
		sol = solve_case(L[idx:idx+N])
		idx+=N
		res.append('Case #' + str(casenr) + ': ' + str(sol) + '\n')
	
	fout = open(out_name, 'w')
	fout.writelines(res)
	fout.close()
	return


#sys.setrecursionlimit(1010)	
#solve('A-test.in', 'A-test.out')	
#solve('A-small-attempt0.in', 'A-small-attempt0.out')
solve('A-large.in', 'A-large.out')
