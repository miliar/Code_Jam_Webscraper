#!/usr/bin/env python

import os, sys, math

def isPalin(s):
    l = len(s)
    if l == 1:
        return True
    h = l / 2

    if s[ : h] == s[-h:][::-1]:
        return True
    return False

golden = {}

def genGolden(low, high):    
    lbound = int(math.sqrt(low))
    if lbound * lbound < low:
        lbound += 1
    
    hbound = int(math.sqrt(high)) + 1
    count = 0
      
    for c in xrange(lbound, hbound):
        s = str(c)
        if (isPalin(s) == False):
            continue
        else:
            c2 = c * c
            s2 = str(c2)
            if (isPalin(s2)):
                golden[c2] = True


f = open(sys.argv[1])
lines = f.readlines()
f.close()

num = int(lines[0].strip())

genGolden(1, 100000000000000)

for case in xrange(1, num + 1):
    a = [int(i) for i in lines[case].split()[:2]]
    low, high = a[0], a[1]
    
    count = 0
    for i in golden.keys():
        if i >= low and i <= high:
            count += 1
    
                    
    print 'Case #%d: %d' % (case, count)
    