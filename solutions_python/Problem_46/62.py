#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys,re

input = 'A-large.in.txt'
output = 'A-large.out.txt'
f = file(input)
g = file(output,'w')

n_cases = int(f.readline().strip())

def getIndex(lines,n):
    for i in range(n,len(lines)):
        if not '1' in lines[i][n+1:]:
            return i

def swap(lines,i,j):
    tmp = lines[j]
    lines[j] = lines[i]
    lines[i] = tmp
    return lines

def swapMany(lines,x,y): #f>t
    for i in range(x,y,-1):
        lines = swap(lines,i-1,i)
    return lines
    
for k in range(n_cases):
    n_lines = int(f.readline().strip())
    
    lines = []
    for i in range(n_lines):
        lines += [f.readline().strip()]
    
    n = 0
    for to in range(n_lines-1):
        fr = getIndex(lines, to)
        swapMany(lines, fr, to)
        n+=fr-to
    
    line = "Case #%d: %d" % (k+1, n)
    
    print line
    g.write("%s\n" % line)

f.close()
g.close()
