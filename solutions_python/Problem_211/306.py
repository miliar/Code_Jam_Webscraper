import networkx as nx
import numpy as np
import math

def intread(): return map(int,raw_input().split())
def floatread(): return map(float,raw_input().split())
def lintread1(n): return [ input() for i in xrange(n) ]
def lintread2(n):
    L1, L2 = [0]*n, [0]*n    
    for i in xrange(n): L1[i],L2[i] = intread()
    return L1, L2
def lintread3(n):
    L1, L2, L3 = [0]*n, [0]*n, [0]*n    
    for i in xrange(n): L1[i],L2[i], L3[i] = intread()
    return L1, L2, L3
def aintread(n): return [ intread() for _ in xrange(n) ]
def adef(a,b,v): return [[v for i in xrange(b)] for j in xrange(a)]

def mull(l):
	r = 1.
	for L in l: r*=L
	return r
def solve(N,K,U,P):
	P.sort()
	if sum(P)+U>=float(K): return 1.
	for k in xrange(K-1,0,-1):
		if P[k]*k <= sum(P[:k])+U:
			v = (sum(P[:k+1])+U)/float(k+1)
			return v**(k+1)*mull(P[k+1:])
	P[0] += U
	return mull(P)

T = input()
for case in xrange(T):
    N,K = intread()
    U = float(raw_input())
    P = map(float,raw_input().split())
    print "Case #"+str(case+1)+":",solve(N,K,U,P)
