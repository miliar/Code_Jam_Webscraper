#! /usr/bin/python

import sys, itertools, operator

def getline():
    return sys.stdin.readline().strip()

def out(s):
    if False:
        print s

def slices(l):
    for x in range(1, len(l)):
        yield l[0:x], l[x:]

def patrickSum(l):
    return reduce(operator.xor, l)

def combos(l, n):
    for indexes in itertools.combinations(range(len(l)), n):
        a, b = [], []
        for i in range(len(l)):
            if i in indexes:
                a.append(l[i])
            else:
                b.append(l[i])
        yield a, b

def solve(casenum):
    N = int(getline())
    nums = [ int(x) for x in getline().split() ]
    nums.sort()
    patrick = nums
    sean = []
    best = 0
    while patrick:
        sean.append(patrick.pop())
        if patrick and patrickSum(patrick) == patrickSum(sean):
            best = max(best, sum(sean), sum(patrick))
    print 'Case #%d: %s' % (casenum, best or 'NO')

cases = int(getline())
for case in xrange(cases):
    solve(case + 1)
