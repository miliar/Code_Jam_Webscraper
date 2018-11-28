#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 18:06:19 2017

@author: leello
"""

def inter(droites, pos, coef, D):
    if droites:
        for i in range(len(droites)):
            a, b = droites[i]
            if a < coef:
                if a * (pos - b)*1.0/(a - coef) + b < D :
                    return inter(droites[i+1:], b, a, D)
        return (coef, pos)
    
    else :
        return (coef, pos)


        
T = int(input())
for i in range(T):
    ans = 0
    D, N = map(int, str(raw_input()).strip("\n").split(" "))
    droites = []
    for k in range(N):
        b, a = map(int, str(raw_input()).strip("\n").split(" "))
        droites.append((b,a))
    droites.sort()
    droites = [(a,b) for b,a in droites]
    c, d = inter(droites[1:], droites[0][1], droites[0][0], D )
    ans = 1.0*c*D*1.0/(D-d)
    print("Case #{0}: {1:.6f}".format(i+1, ans))