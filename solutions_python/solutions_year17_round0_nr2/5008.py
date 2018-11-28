#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 04:39:19 2017

@author: dhruvmehra
"""

import sys

def solve(s):
    while (int(s) >= 0):
        v = 0
        for i in range(1,len(s)):
            if s[i] >= s[i-1]:
                v += 1
                #print ("hi")
            elif s[i] < s[i-1]:
                s = str(int(s)-1)
                break

        if v == len(s)-1:
            return s
print

if __name__ == "__main__":
    f = sys.stdin
    if len(sys.argv) >= 2:
        fn = sys.argv[1]
        ot = sys.argv[2]
        if fn != '-':
            f = open(fn)
            out = open(ot, 'w+')
    
    j = 0
    for line in f:
        j += 1
        if j > 1:
            num2 = solve(str.strip(str(line)))
            print ("Case #{}: {} {}\n". format(j-1, line, num2))
            out.write("Case #{}: {}\n". format(j-1, num2))

