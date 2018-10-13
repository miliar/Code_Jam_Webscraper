#! /usr/bin/env python3

import sys
from heapq import heappush, heappop
from math import floor 

def solve(problem):
    (n, k) = problem

    heap = []
    heappush(heap, (-n, 1, n))

    l = 0
    while heap:
        l += 1
        (m, a, b) = heappop(heap)
        q = floor((a + b) / 2)
        p1 = (- (q-a), a, q-1)
        p2 = (- (b-q), q+1, b)
        if l == k: break
        if p1[0] < 0: heappush(heap, p1)
        if p2[0] < 0: heappush(heap, p2)

    x = [-p1[0], -p2[0]]
    x.sort()
    return '{} {}'.format(x[1], x[0])

def parse(content):
    lines = content.split('\n')
    T = int(lines[0])
    return [(int(n), int(k)) for (n, k) in map(str.split, lines[1:T+1])]

#################################################################

if __name__ == '__main__':
    filename = sys.argv[1]

    with open(filename) as f:
        content = f.read().strip()

    with open(filename + '.out', 'w') as out:   
        for (i, case) in enumerate(parse(content), 1):
            result = solve(case)
            for o in (out, sys.stdout):
                print('Case #', i, ': ', result, sep='', file=o)
