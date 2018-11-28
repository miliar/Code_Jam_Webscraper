# -*- coding: utf-8 -*-

import os,sys
import math

def jamout(linestring):
    if istest:
        print linestring
    else:
        fo.write(linestring + '\n')
        print linestring


        
ex = """4
4 11111
1 09
5 110011
0 1
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
board = []
for i in range(T):
    l = lines[cursor]
    cursor += 1
    smax,slst = l.split(' ')
    
    slst = [int(s) for s in slst]
    
    print smax, slst
    cnt = 0
    cntfr = 0
    for idx, s in enumerate(slst):
        if s>0 and cnt < idx:
            cntfr += idx - cnt
            cnt += cntfr
        cnt += s   
    result = cntfr
    jamout("Case #%d: %d" % (i+1, result))

if istest==False:
    fo.close()