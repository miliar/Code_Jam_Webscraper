#!/usr/bin/env python
#coding=utf-8
import copy

##inPath = 'test.in'
##outPath = 'test.out'
inPath = 'B-small-attempt0.in'
outPath = "B-small-attempt0.out"
##inPath = 'B-large.in'
##outPath = "B-large.out"

def count(a, b, k):
    if a >= b:
        smal = b
        big = a
    else:
        smal = a
        big = b
    res = 0
##    for i in xrange(1, smal + 1):
####        for j in xrange(1, i):
####            if i & j < k:
####                res += 2
####        if i & i < k:
####            res += 1
##        for j in xrange(1, i + 1):
##            if i & j < k:
##                res += 2
##    for i in xrange(smal + 1, big + 1):
##        for j in xrange(1, smal + 1):
##            if i & j < k:
##                res += 1
    for i in xrange(smal):
        for j in xrange(i):
            if i & j < k:
                res += 2
        if i & i < k:
            res += 1
    for i in xrange(smal, big):
        for j in xrange(smal):
            if i & j < k:
                res += 1
            
    return res
    

with open(outPath,'w') as outf:
    with open(inPath) as inf:
        n = int(inf.readline().strip())
        for case in xrange(1, n+1):
            a, b, k = map(int, inf.readline().strip().split())
##            print type(a), b, k 4
            outf.write("Case #" + str(case) + ": " + str(count(a, b, k)) + '\n')
##            if SWITCH == LEN + 1:
##                outf.write("Case #" + str(case) + ": NOT POSSIBLE\n") 
##            else:
##                outf.write("Case #" + str(case) + ": " + str(SWITCH) + '\n')
