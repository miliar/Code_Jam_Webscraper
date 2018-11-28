# -*- coding: utf-8 -*-

import os,sys
import math
from copy import deepcopy

def jamout(linestring):
    if istest:
        print linestring
    else:
        fo.write(linestring + '\n')
        print linestring

def solve(x,y,lw,flg,mx):
    w = len(lw[0])
    h = len(lw)

    if lw[y][x]<mx and flg[y][x] == 0:
        flg[y][x]=1
        if x-1>=0: solve(x-1,y,lw,flg,mx)
        if x+1< w: solve(x+1,y,lw,flg,mx)
        if y-1>=0: solve(x,y-1,lw,flg,mx)
        if y+1< h: solve(x,y+1,lw,flg,mx)

ex = """3
3 3
2 1 2
1 1 1
2 1 2
5 5
2 2 2 1 2
2 3 2 1 2
2 2 2 1 2
2 2 3 1 1
2 2 2 1 2
1 3
1 2 1
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
    N,M = [int(p) for p in param.split(' ')]
    cursor += 1
    lawn = []
    lawntmp = []
    lawnflg = [[0 for x in range(M)] for y in range(N)]
    
    for y in range(N):
        line = lines[cursor]
        row = [int(p) for p in line.split(' ')]
        lawn.append(row)
        cursor += 1
    
    mxheight = 1
    for y in range(N):
        for x in range(M):
            if mxheight<lawn[y][x]: mxheight=lawn[y][x]
    lawntmp = [[mxheight for x in range(M)] for y in range(N)]
    
    
    for y in range(N):
        mx0 = 1
        mx1 = 1
        for x in range(M):
            if mx0<lawn[y][x]: mx0=lawn[y][x]
            if mx1<lawntmp[y][x]: mx1=lawntmp[y][x]
        if mx1>mx0:
            for x in range(M):
                lawntmp[y][x]=mx0
    for x in range(M):
        mx0 = 1
        mx1 = 1
        for y in range(N):
            if mx0<lawn[y][x]: mx0=lawn[y][x]
            if mx1<lawntmp[y][x]: mx1=lawntmp[y][x]
        if mx1>mx0:
            for y in range(N):
                lawntmp[y][x]=mx0
        
    #print lawntmp
    
    result = 'YES'
    for y in range(N):
        if lawn[y]!=lawntmp[y]:
            result = 'NO'
            break
    jamout("Case #%d: %s" % (i+1, result))

if istest==False:
    fo.close()