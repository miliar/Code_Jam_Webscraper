# -*- coding: utf-8 -*-
"""
Created on Sat Apr 08 17:45:26 2017

@author: sanindra
"""

def tidyN(n):
    n = str(n)
    if len(n)==1: return True
    for i in xrange(len(n)-1):
        if int(n[i])>int(n[i+1]):
            return False  
    return True

def findNext(n):
    n = str(n)
    for i in xrange(len(n)-1):
        if int(n[i])>int(n[i+1]):
            n = n[:i] + str(int(n[i])-1)+ '9'* (len(n)-(i+1))
    return int(n)

t = input()

for i in xrange(t):
    n, x = input(), 0
    while n> 0:
        if tidyN(n):
             x= n
             break
        n = findNext(n)
    print "Case #{}: {}".format(i+1,x)