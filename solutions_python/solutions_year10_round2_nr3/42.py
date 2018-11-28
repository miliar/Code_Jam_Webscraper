#!/usr/bin/env python
# -*- coding: utf-8 -*-

# (c) DDPAlphaTiger1 2010
# Will be under GPL after the end of GCJ
# Under no-use-by-anyone-else-than-me license until then :D
# ***** *****
# Thanks for reading my weird code !
# ***** *****
# Note : I have a wiiide screen, that helps ...

import sys

import psyco
psyco.full()

def trynumlist(n, l):
    try:
        i = l.index(n)
        if i == 0:
            return 1
        else:
            return trynumlist(i+1,l)
    except:
        return 0

def listoflists(k, n):
    if k == n:
        return (1, [[n]])
    if k == 2:
        (tot, l1) = listoflists(k+1, n)
        for x in l1:
            l3 = [2]
            l3.extend(x)
            tot += trynumlist(n, l3)
        return (tot, [])
    else:
        (tot, l1) = listoflists(k+1, n)
        l2 = []
        for x in l1:
            l2.append(x)
            l3 = [k]
            l3.extend(x)
            tot += trynumlist(n, l3)
            l2.append(l3)
        return (tot, l2)

d = {}
for num in range(2, 26):
    print num
    (dnum, lol) = listoflists(2, num)
    d[num] = dnum
    print (num, d[num])
print d
