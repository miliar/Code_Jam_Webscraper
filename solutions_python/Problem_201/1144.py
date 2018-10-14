#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 18:58:57 2017

@author: marshi
"""

import numpy as np 

#def bathroom(n,k):
#    empty = [n]
#    for i in range(k):
#        space = empty.pop(-1)
#        space -= 1
#        max_emp,min_emp = space-space//2,space//2
#        empty.append(max_emp)
#        empty.append(min_emp)
#        empty = sorted(empty)
#    return max_emp,min_emp
    
def bathroom(n,k):
    empty = [n]
    for i in range(k):
        space = empty.pop(empty.index(max(empty)))
        space -= 1
        max_emp,min_emp = space-space//2,space//2
        empty.append(max_emp)
        empty.append(min_emp)
    return max_emp,min_emp

def bathroom2(n,k):
    k_2 = 2**int(np.log2(k))-1
    res_space = n-k_2
    res_k = k-k_2
    space = res_space // (k_2+1)
    space_plus_num = res_space % (k_2+1)
    if res_k <= space_plus_num:
        obj_space = space
    else:
        obj_space = space-1
    max_emp,min_emp = obj_space-obj_space//2,obj_space//2
    return max_emp,min_emp

n_ = int(input())
for i in range(n_):
    n,k = map(int,input().split(' '))
    ret1,ret2 = bathroom2(n,k)
    print('Case #%d: %d %d'%(i+1,ret1,ret2))
