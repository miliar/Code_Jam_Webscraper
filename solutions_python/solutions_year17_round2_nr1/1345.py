# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 02:44:21 2017

@author: Ghomam
"""

import sys

#Open Test file
f = open(sys.argv[1])
data = f.readlines()
f.close()

# Input
finish = False
lines = int(data[0].strip().replace('\n',''))+1
index = 1
tests = []
while index<lines:
    temp = data[index].strip().replace('\n','')
    d0, C = [ int(n) for n in temp.split(' ') ]
    lines += C
    M = [ d0*1. ]
    index += 1
    for c in range(C):
        d, v = [ int(v) for v in data[index].replace('\n','').split(' ') ]
        M += [ (d0 - d*1.)/v ]
        index += 1
    tests.append( M )

output = []
for test in tests:
    output += [test[0]/max(test[1:])]

#Output
result = open(sys.argv[1].replace('in', 'out'), 'w')
for i, r in enumerate(output):
    out = 'Case #{}: {}\n'.format(i+1, str(r))
    print out[:-1]
    result.write(out)
result.close()