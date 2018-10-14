#!/bin/python
import sys
from math import *
input_filename, = sys.argv[1:]
input = open(input_filename)
assert input_filename.endswith('.in'), input_filename
output = open(input_filename[:-3]+'.out', 'w')

from collections import defaultdict

def run():
    N, K = map(int,input.readline().split())
    print N,K
    assert K > 0
    lst = []
    for i in range(N):
        lst.append(map(int,input.readline().split()))
    def f(r,h):
        return pi*r * (r + 2 * h)
    assert len(lst) == N
    lst.sort(key=lambda (r,h): -r*h)
    print lst

    results = []
    
    for i in range(N):
        a = 0.0
        a += f(lst[i][0],lst[i][1])
        REST = lst[:i] + lst[i+1:]
        REST = [x for x in REST if x[0] <= lst[i][0]]
        print "REST", REST
        if len(REST) >= K-1:
            for (r,h) in REST[:K-1]:
                a += 2* pi * r*h
            results.append(a)
    print "results", results
    return max(results)
    
T = int(input.readline())
for t in range(T):
    print >> output, 'Case #{}: {:.20f}'.format(t+1,run())
