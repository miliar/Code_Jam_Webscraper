#! /usr/bin/env python

import sys, copy, numpy
from copy import copy

f = file(sys.argv[1])
lines = [ln.strip() for ln in f.readlines()]
T = int(lines[0])
print('%s contains %i (T) test cases' % (sys.argv[1],T))

cases = []
ind = 1
for i in range(T):
    #print(lines[ind], lines[ind].split(' '))
    N = int(lines[ind])
    Avals, Bvals = [],[]
    for i in range(N):
        ind = ind + 1
        a,b = [int(k) for k in lines[ind].split(' ')]
        Avals.append(a)
        Bvals.append(b)
    ind = ind + 1
    cases.append([N,Avals,Bvals])
print(cases)

def ropeProblem(N,Avals,Bvals):
    '''
    You've noticed that no two wires share an endpoint (in other words, there's at most one wire going out of each window). However, from your viewpoint, some of the wires intersect midway. You've also noticed that exactly two wires meet at each intersection point.
    
    On the above picture, the intersection points are the black circles, while the windows are the white circles.
    
    How many intersection points do you see?
    Input

    The first line of the input gives the number of test cases, T. T test cases follow. Each case begins with a line containing an integer N, denoting the number of wires you see.

    The next N lines each describe one wire with two integers Ai and Bi. These describe the windows that this wire connects: Ai is the height of the window on the left building, and Bi is the height of the window on the right building. 
    '''
    #sorting according to avalue
    AB_sorted = sorted(zip(Avals,Bvals))
    #print(AB_sorted)
    Avals = [AB[0] for AB in AB_sorted]
    Bvals = [AB[1] for AB in AB_sorted]
    #print(Avals,Bvals)

    intersections = 0
    for i in range(N-1):
        intersections = intersections + sum([Bv < Bvals[i] for Bv in Bvals[i+1:]])
    return intersections


results = []
for t in range(T):
    print('case %i of %i' % (t+1,T))
    print(cases[t])
    res = ropeProblem(*cases[t])
    results.append('Case #%i: %i' % (t+1,res))
    print(results[-1])

f = file(sys.argv[1].replace('.in','.out'),'w')
f.write('\n'.join(results))
f.close()
