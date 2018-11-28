#!/usr/bin/python

__author__ = "Thomas van den Berg"

# from itertools import izip, permutations
import numpy as np
import math
from pprint import pprint

def avg(l):
    return sum(l)/float(len(l))

fn = 'B-small-attempt0.in'
f = open(fn,'r')
fout = open(fn.replace('.in','.out'),'w')

def centered(arr, xb, xe, yb, ye):
    section = arr[yb:ye,xb:xe]
    ysum = section.sum(axis=0)
    xsum = section.sum(axis=1)
    tl = section[0,0]
    tr = section[0,-1]
    bl = section[-1,0]
    br = section[-1,-1]

    
    ysum[0] -= (tl+bl)
    ysum[-1] -= (tr+br)
    xsum[0] -= (tl+tr) 
    xsum[-1] -= (bl+br)
    
    l = (xe-xb)-1
    s = (xe-xb)//2
    
    for i in xrange(s):
        if ysum[i] != ysum[l-i]:
            return False
        if xsum[i] != xsum[l-i]:
            return False
    return True

T = int(f.readline())
for case in xrange(T):
    
    (R,C,D) = [int(d) for d in f.readline().split()]
    
    arr = []
    for r in xrange(R):
        row = [int(d) for d in f.readline().replace('\n','')]
        arr.append(row)
    nparr = np.array(arr)
    S = min(R,C)
    s = S
    found = False
    for s in xrange(S-2):
        s = S-s
        for i in xrange((R-s)+1):
            for j in xrange((C-s)+1):
                found = centered(nparr, j,j+s,i,i+s)
                if found:
                    break
            if found: 
                break
        if found: 
            break
    ans = s if found else "IMPOSSIBLE"
    print ans
    fout.write('Case #%d: %s\n'%(case+1,ans))
    
