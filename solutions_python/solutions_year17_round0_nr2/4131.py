#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 13:09:08 2017

@author: psalm
"""

def is_sorted(n: int) -> int:
    digits = [int(d) for d in str(n)]
    if len(digits) == 1:
        return True
    else:
        k = 1
        while k < len(digits):
            if digits[k-1] > digits[k]:
                return False
            else:
                k += 1
        return True
    
    
def find_last_tidy(n: int) -> int:
    digits = [int(d) for d in str(n)]
    k = 1
    while k < len(digits):
        if digits[k-1] > digits[k]:
            for i in range(k, len(digits)):
                digits[i] = 9
            digits[k-1] -= 1
            k = 1
        else:
            k += 1
    
    num = int("".join([str(d) for d in digits]))
    return(num)
    
t = int(input())
for i in range(1,t+1):
    N = int(input())
    last_tidy = find_last_tidy(N)
    print("Case #{}: {}".format(i, last_tidy))