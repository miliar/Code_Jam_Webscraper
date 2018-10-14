#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 17:23:58 2017

@author: tianxia
"""

f = open("B-Large.in.txt")
w = open("B-Large.out.txt", "w")
t = int(f.readline())
for ti in range(1, t+1):
    s = f.readline().strip()
    #print(s)
    m = 0
    d = True
    for i in range(1, len(s)):
        if s[i] > s[i-1]:
            m = i
        elif s[i] < s[i-1]:
            d = False
            break
    if d:
        res = s
    else:
        number = int(s[:m+1] + "0"*(len(s)-1-m)) - 1
        res = str(number)
    print(s, res)        
    w.write("Case #%d: %s\n" % (ti, res))
w.close()