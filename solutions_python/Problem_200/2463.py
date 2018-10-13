# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 08:33:57 2017

@author: arena
"""
def tidy_up(num):
    end = len(num)
    for i in range(1, end):
        if num[i-1] > num[i]:
            num[i-1] -= 1
            num[i:] = [9 for k in range(i, end)]
    return num

T = int(input())
for t in range(T):
    N = input()
    str_n = [int(_) for _ in N]
    for end in range(len(str_n), 1, -1):
        str_n = tidy_up(str_n[:end]) + str_n[end:]
        if str_n == sorted(str_n, reverse = True):
            break
    N = [str(k) for k in str_n]
    print("Case #" + str(t+1) + ": ", end = "")
    print("".join(N).lstrip("0"))
    
