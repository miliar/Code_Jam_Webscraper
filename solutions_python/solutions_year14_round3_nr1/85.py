#import sys
#import numpy as np
#import random as rnd
#from math import log, pi

def gcd(a,b):
	if a<b:
		a,b = b,a
	while a>b and b>0:
		a, b = b, a%b
	return a
		
def getBin(x):
	L = []
	while(x>0):
		L.append(x%2)
		x>>=1
	L.reverse()
	return L
	
def getNr(L):
	x = 0
	for i in L:
		x <<= 1
		x += i
	return x


def solve_case(P, Q):
	G = gcd(P, Q)
	P//=G
	Q//=G
	Qb = getBin(Q)
	if(sum(Qb)>1):
		return 'impossible'
	else:
		ndoub = 0
		while(P<Q):
			P*=2
			ndoub+=1
		return ndoub
	
	return 0			

def solve(in_name, out_name):
	fin = open(in_name, 'r');
	L = [map(int, x.strip().split('/')) for x in fin.readlines()]
	fin.close()
		
	res = []	
	for casenr in xrange(1, len(L)):
		P, Q = L[casenr]
		sol = solve_case(P, Q)
		res.append('Case #' + str(casenr) + ': ' + str(sol) + '\n')
	
	fout = open(out_name, 'w')
	fout.writelines(res)
	fout.close()
	return


#sys.setrecursionlimit(1010)	
#solve('A-test.in', 'A-test.out')	
#solve('A-small-attempt0.in', 'A-small-attempt0.out')
solve('A-large.in', 'A-large.out')
