#!/usr/bin/python
import sys
import numpy as np     # http://www.numpy.org/
import scipy           # http://scipy.org/
import networkx as nx  # https://networkx.github.io/
import sympy           # http://www.sympy.org


T = int(sys.stdin.readline())

solutions = []

def solve(N,mi):
    assert( N == len(mi) )
    eaten = 0
    last = 0
    for i in range(0,N):
        if last>mi[i]: eaten += last-mi[i]
        last = mi[i]
    result = "%s " % (eaten)


    eaten = 0
    last = 0
    speed = 0
    total = 0
    for i in range(1,N):
        speed = max(speed,mi[i-1]-mi[i])
    for i in range(1,N):
        if mi[i-1] < speed:
            total += mi[i-1]
        else:
            total += speed
    
    result += str(total)
    return result
    
    
for case in range(0, T):
    solution = ""
    N = int(sys.stdin.readline())
    mi= map(int,sys.stdin.readline().strip().split())
    solution = solve (N,mi)
    solutions.append(solution)

for case in range(0, T):
    print "Case #%i: %s" % (case + 1, solutions[case])
