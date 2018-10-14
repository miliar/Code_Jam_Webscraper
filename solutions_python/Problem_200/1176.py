#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 18:14:25 2017

@author: marshi
"""


def is_tidy(n):
    n = str(n)
    n = [int(n_) for n_ in n]
    ret = [n[i]<=n[i+1] for i in range(len(n)-1)]
    return all(ret)

def to_tidy(n):
    for i in range(n,0,-1):
        if is_tidy(i):
            break
    return i

def to_tidy2(n):
    if is_tidy(n):
        return n
        
    n = str(n)
    n = [int(n_) for n_ in n]
    ret = [n[i]<=n[i+1] for i in range(len(n)-1)]

    cng = ret.index(False)
    cng = n.index(n[cng])
    n[cng] -= 1
    n[cng+1:] = [9 for _ in n[cng+1:]]
    n = [str(n_) for n_ in n]
    n = ''.join(n)
    n = int(n)
    return n

n = int(input())
for i in range(n):
    n_ = int(input())
    print('Case #%d: %d'%(i+1,to_tidy2(n_)))

