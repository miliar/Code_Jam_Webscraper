# -*- coding: utf-8 -*-
"""

@author: Saurav Kanchan

"""
def isTidy(n):
    s=str(n)
    for i in range((len(s))-1):
        if int(s[i])>int(s[i+1]):return False
    return True

for t in range(1,int(input())+1):
    for i in range(int(input()),0,-1):
        k=isTidy(i)
        if k:
            print("Case #{0}: {1}".format(t,i))
            break