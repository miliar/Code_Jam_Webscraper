#!/usr/bin/env python2
# -*- coding: utf-8 -*-


# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

colors = ('R', 'O', 'Y', 'G', 'B', 'V')

bcs = ('R', 'Y', 'B')

testCaseTotal = int(raw_input())  # read a line with a single integer
for testCase in xrange(1, testCaseTotal + 1):
    templst = [int(s) for s in raw_input().split(" ")]
    N = templst[0]
    hs = templst[1:]
    reds = hs[0]
    yellows = hs[2]
    blues = hs[4]
    
    isPossible = True
    for i in xrange(6):
        if hs[i] > N/2:
            isPossible = False
            break
    if isPossible:
        fhs = (reds, yellows, blues)
        
        lst = [[fhs[i], bcs[i]] for i in xrange(3)]
        slst = sorted(lst)
        
        result = ['*' for i in xrange(N)]
        index = 0
        for j in xrange(slst[2][0]):
            result[index] = slst[2][1]
            index += 2
        for j in xrange(slst[1][0]):
            if (index >= N):
                index = 1
            result[index] = slst[1][1]
            index += 2
        for j in xrange(slst[0][0]):
            if (index >= N):
                index = 1
            result[index] = slst[0][1]
            index += 2
        
        result = ''.join(result)
    else:
        result = "IMPOSSIBLE"
        
    print "Case #{}: {}".format(testCase, result)
