#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

fin = open('watert.in','r')
N = int(fin.readline()[:-1])
for n in range(N):
    H, W = [int(c) for c in fin.readline()[:-1].split()]
    map = []
    for h in range(H):
        map.append( [int(c) for c in fin.readline()[:-1].split()] )
    res = [[0 for w in range(W)] for h in range(H)]
    alp = 0
    for h in range(H):
        for w in range(W):
            l = [[h,w]]
            while len(l):
                cur = l[-1]
                hh,ww = cur
                if res[hh][ww] > 0:
                    for cur in l:
                        res[cur[0]][cur[1]] = res[hh][ww]
                    l =[]
                else:
                    next = [ [map[hh+dh][ww+dw], dir]  for dir, dh, dw in [[0,-1,0], [1,0,-1], [3,1,0], [2,0,1]] if 0<= hh+dh < H and 0<= ww+dw < W and map[hh][ww] > map[hh+dh][ww+dw]] 
                    if next == []:
                        alp += 1
                        for cur in l:
                            res[cur[0]][cur[1]] = alp
                        l =[]
                    else:
                        q = sorted(next)[0][1]
                        l.append( [hh-(q==0)+(q==3), ww-(q==1)+(q==2)] )

    print "Case #"+str(n+1)+":"
    for s in res:
        st = ""
        for c in range(len(s)):
            st += chr(s[c]+96) + " "*(c<len(s)-1)
        print st
