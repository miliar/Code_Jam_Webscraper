#!/usr/bin/python

import sys
from math import log10

def isRecycled(n,m):
    #print n,m
    N, M = str(n), str(m)
    #check = int(log10(m)) - int(log10(n))
    #if check:
    if len(N) != len(M):
        return False
    for i in range(1,len(str(n))):
        if N[:i] == M[-i:] and N[i:] == M[:-i]:
            return True
    return False

def compute(A,B):
    count = 0
    for n in xrange(A,B):
        for m in xrange(n+1, B+1):
            if isRecycled(n,m):
                count += 1
    return count       

inputs = []
with open(sys.argv[1], 'r') as f:
    n = int(f.readline().strip())
    for l in f:
        T = l.split()
        if len(T):
            inputs.append((int(T[0]), int(T[1])))

print inputs
s = ""
for i,(A,B) in enumerate(inputs):
    s += 'Case #%i: ' % (i+1)
    s += str(compute(A,B))
    s += '\n'

print s,
with open(sys.argv[1] + '.out', 'w') as f:
    f.write(s)
        
    

