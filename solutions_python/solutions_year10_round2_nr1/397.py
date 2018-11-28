#!/usr/bin/python

import re, sys

T = int(raw_input())

for t in xrange(1,T+1):
    bounds = map(int, sys.stdin.readline().split())
    N = bounds[0]
    M = bounds[1]

    tree = {'/':True}
    want = []
    for n in xrange(0,N):
        path  = sys.stdin.readline().rstrip('\n')
        xs = path.split('/')
        y = ''
        for x in xs[1:]:
            y += '/' + x
            tree[y] = True
    for m in xrange(0,M):
        want.append(sys.stdin.readline().rstrip('\n'))
    want.sort()

    count = 0
    for path in want:
        xs = path.split('/')
        y = ''
        for x in xs[1:]:
            y += '/' + x
            if y not in tree:
                count += 1
                tree[y] = True
    line = 'Case #' + str(t) + ': ' + str(count)
    print line
