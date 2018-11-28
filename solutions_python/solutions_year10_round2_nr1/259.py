#! /usr/bin/python

import sys

def getline():
    return sys.stdin.readline().strip()

def solve(casenum):
    n, m = [ int(x) for x in getline().split() ]
    cur = {'/': 1}
    for x in range(n):
        cur[getline()] = 1
    new = {}
    for x in range(m):
        path = getline()
        new[path] = len(path.split('/')) - 1
    paths = new.keys()
    paths.sort(cmp=lambda a, b: cmp(new[a], new[b]))
    answer = 0
    for path in paths:
        while path and not path in cur:
            cur[path] = 1
            answer += 1
            path = path[:path.rindex('/')]
    print 'Case #%d: %s' % (casenum, answer)

cases = int(getline())
for case in xrange(cases):
    solve(case + 1)

