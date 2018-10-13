#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 03:20:23 2017

@author: leello
"""
def istidy(n):
    if n<10:
        return True
    N = str(n)
    L = map(int, list(N))
    res = True
    for i in range(1, len(L)):
        res = res and L[i-1] <= L[i]
    return res

def build(b):
    if b == [0]:
        return ''
    if len(b) == 1:
        return str(b[0])
    if b[0] < b[1]:
        b[1] -= 1
        return build(b[1:]) + '9'
    else:
        ans = build(b[1:])
        if ans[-1] == '9':
            return ans + '9'
        else:
            return ans + str(b[0])
        

T = int(input())
for i in range(T):
    N = int(input())
    L = map(int, list(str(N)))
    #print("Case #{0}: {1}".format(i+1, N))
    print("Case #{0}: {1}".format(i+1, build(L[::-1])))
    
    