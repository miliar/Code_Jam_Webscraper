#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 16:58:18 2017

@author: tianxia
"""

f = open("A-large.in.txt")
w = open("A-large.out.txt", "w")
t = int(f.readline())
for ti in range(1, t+1):
    s, size = f.readline().strip().split()
    s = list(s)
    size = int(size)
    count = 0
    #print(s)
    for i in range(len(s)-size+1):
        if s[i]=="-":
            count += 1
            for j in range(i, i+size):
                if s[j]=="-":
                    s[j] = "+"
                else:
                    s[j] = "-"
            #print(s)
    valid = True
    for i in range(max(0, len(s)-size), len(s)):
        if s[i] == "-":
            valid = False
            break
    if valid:
        res = str(count)
    else:
        res = "IMPOSSIBLE"
            
    w.write("Case #%d: %s\n" % (ti, res))
w.close()