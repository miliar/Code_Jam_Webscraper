#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 13:18:40 2017

@author: lyj
"""
def findtidy(numlist):
    
    length = len(numlist)
    if length == 1:
        return numlist
    i = 0
    while numlist[i] == numlist[i+1]:
        if i == length - 2:
            return numlist
        i += 1
    if numlist[i+1] > numlist[i]:
        return numlist[0:i+1] + findtidy(numlist[i+1:])
    else:
        numlist[0] -= 1
        for i in range(1, len(numlist)):
            numlist[i] = 9
        return numlist
    

T = int(raw_input())
for i in range(T):            
    N = int(raw_input())
    numlist = [int(d) for d in str(N)]
    numList = findtidy(numlist)
    print "Case #" + str(i+1) + ":", int(''.join(map(str,numList)))    