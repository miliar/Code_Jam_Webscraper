#!/usr/bin/python
import sys
import numpy as np     # http://www.numpy.org/
import scipy           # http://scipy.org/
import networkx as nx  # https://networkx.github.io/
import sympy           # http://www.sympy.org
import itertools
import operator
import string

sys.setrecursionlimit(5000)

T = int(sys.stdin.readline())

def cca(a,b):
    T=max(a,b)
    if T>0: return (abs(a-b)<1e-6) or abs(a-b)/T<1e-6
    return (abs(a-b)<1e-6)

def solve(Ri,Ci,N,V,X):
    if N==1:
        if X!=Ci[0]: return "IMPOSSIBLE"
        return "%f" % (V/Ri[0])

    if N==2:
        if Ci[1]<X or Ci[0]>X: return "IMPOSSIBLE"
        if (Ci[1]-Ci[0])<1e-6 or (Ci[1]-Ci[0])/Ci[0]<1e-6:
            time = V / sum(Ri)
            return "%f" % time
        ratio = 1.0 - (X-Ci[1])/ (Ci[0]-Ci[1])
        time = max(V*ratio / Ri[1],V*(1-ratio) / Ri[0])
        return "%f" % time


for case in range(0, T):
    N,V,X = sys.stdin.readline().strip().split()
    N=int(N)
    V=float(V)
    X=float(X)
    Ri=[]
    Ci=[]
    for i in range(N):
        r,c= map(float,map(string.strip,sys.stdin.readline().strip().split()))
        Ri.append(r)
        Ci.append(c)
    if N==2 and Ci[0]>Ci[1]:
            Ri.reverse()
            Ci.reverse()
    solution = solve(Ri,Ci,N,V,X)
    print "Case #%i: %s" % (case + 1, solution)

