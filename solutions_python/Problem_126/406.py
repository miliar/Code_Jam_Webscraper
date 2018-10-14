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
quartz 1
straight 3
gcj 2
tsetse 2
aeoiu 1
"""

def check_conso(nam, n):
    cnt = 0
    isstart = False
    for c in nam:
        if c not in ['a','e','i','o','u']:
            if isstart:
                cnt += 1
            else:
                cnt = 1
                isstart = True
            if cnt==n:
                return True
        else:
            isstart = False
    return False

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
    name,n = [p for p in param.split(' ')]
    n = int(n)
    l = len(name)
    cursor += 1
    
    result = 0
    for x in range(l):
        for y in range(l-x+1):
            if y>=n:
                #print name[x:x+y]
                if check_conso(name[x:x+y],n):
                    result += 1
    
    jamout("Case #%d: %s" % (i+1, result))

if istest==False:
    fo.close()