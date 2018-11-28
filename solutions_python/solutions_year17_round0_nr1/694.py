#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 22:30:50 2017

@author: ansli
"""
def flipOne(a):
    if a == '+':
        return '-'
    elif a == '-':
        return '+'
    else:
        raise Exception("Wrong input: " + a)

def flip(p, index, num):
    return p[:index] + ''.join(map(flipOne, list(p[index : index+num]))) + \
           p[index+num:]

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    pancake, strNum = raw_input().split(" ")  # read a list of integers, 2 in this case
    num = int(strNum)
    pl = len(pancake)
    
    flipCount = 0
    for index in range(0, pl - num + 1):
        if pancake[index] == '-':
            pancake = flip(pancake, index, num)
            flipCount += 1
    
    if pancake[pl-num:] == '+' * num:
        result = flipCount
    else:
        result = "IMPOSSIBLE"
            
    print "Case #{}: {}".format(i, result)
    
#print d