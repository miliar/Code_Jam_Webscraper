import networkx as nx
import numpy as np
import math
import itertools as it

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

def solve(N,K,R,H):
	x = 0
	for l in it.combinations(xrange(N),K):
		v = max([R[i] for i in l])**2 + sum([H[i]*2*R[i] for i in l])
		x = max(x,v)
	return x*math.pi
T = input()
for case in xrange(T):
    N,K = intread()
    R,H = lintread2(N)
    print "Case #"+str(case+1)+":","{0:.10f}".format(solve(N,K,R,H))
