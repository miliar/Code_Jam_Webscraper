# -*- coding: utf-8 -*-

import os,sys
import math

def jamout(linestring):
    if istest:
        print linestring
    else:
        fo.write(linestring + '\n')
        print linestring


        
ex = """5
1 9
1 10
3 40
1 1000000000000000000
10000000000000000 1000000000000000000
"""

if len(sys.argv)==3:
    infile  = sys.argv[1]
    outfile = sys.argv[2]
    fo = open(outfile,'w')
    s = open(infile, 'r').read()
    lines = s.split('\n')
    istest = False
else:
    lines = ex.split('\n')
    istest = True

T = int(lines[0])
cursor = 1

for i in range(T):
    param = lines[cursor]
    r,t = [int(p) for p in param.split(' ')]
    cursor += 1
    
    a = 2
    b = 2*r -1
    c = -t
    n0 = (-b+math.sqrt(b*b-4*a*c))/(2*a)
    n1 = (-b-math.sqrt(b*b-4*a*c))/(2*a)
    if n0>n1:
        n = int(n0)
    else:
        n = int(n1)
    result = 0
    
    for j in range(n-1,n+3):
        sum = (2*j*j-j+2*r*j)
        if t == sum:
            result = j
            break
        elif t<sum:
            result = j-1
            break
    jamout("Case #%d: %s" % (i+1, result))

if istest==False:
    fo.close()