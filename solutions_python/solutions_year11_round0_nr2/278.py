#!/usr/bin/python

__author__ = "Thomas van den Berg"

from itertools import izip, permutations
from numpy import *

fn = 'B-large.in'
f = open(fn,'r')
fout = open(fn.replace('.in','.out'),'w')

T = int(f.readline())
for case in xrange(T):
    
    # Parse input
    rest = f.readline().split()
    C = int(rest[0])
    combinations = rest[1:C+1]
    rest = rest[C+1:]
    D = int(rest[0])
    opposed = rest[1:D+1]
    rest = rest[D+1:]
    N = rest[0]
    invoke = rest[1]
    
    # Precompute
    combiners = {}
    for c in combinations:
        combiners[c[0]+c[1]] = c[2]
        combiners[c[1]+c[0]] = c[2] 
    
    # Invoking
    result = ''
    for letter in invoke:
        result += letter
        
        # Combine
        if result[-2:] in combiners:
            nonbase = combiners[result[-2:]]
            result = result[:-2] + nonbase
        
        # Oppose
        for a, b in opposed:
            if a in result and b in result:
                result = ''
    
    ans = '['+', '.join(result)+']'
    fout.write('Case #%d: %s\n'%(case+1,ans))
    
