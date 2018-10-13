#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 18:03:36 2017

@author: marshi
"""


def flipper(s,k):
    '''
    s:str(ex '-++')
    k:str(ex '3')
    '''
    k = int(k)
    s = [1 if c=='+' else 0 for c in s]
    flip_range = len(s)-k+1
    ret = 0
    for i in range(flip_range):
        if s[i] == 0:
            s[i:i+k] = [(s[j]+1)%2 for j in range(i,i+k)]
            ret += 1
    if sum(s)==len(s):
        return str(ret)
    else:
        return 'IMPOSSIBLE'

n = int(input())
for i in range(n):
    s,k = input().split(' ')
    ret = flipper(s,k)
    print('Case #%d: %s'%(i+1,ret))