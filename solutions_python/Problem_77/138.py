#! /usr/bin/python

import sys, itertools

def getline():
    return sys.stdin.readline().strip()

def out(s):
    if False:
        print s

def solve(casenum):
    N = int(getline())
    nums = [ int(x) for x in getline().split() ]
    right = 0
    for i in range(N):
        if nums[i] == i + 1:
            right += 1
    print 'Case #%d: %f' % (casenum, N - right)

cases = int(getline())
for case in xrange(cases):
    solve(case + 1)
