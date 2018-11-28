#!/usr/bin/env python2.7
from __future__ import print_function

def elem_pair((a,b)):
    return(min(a,b), max(a,b)) 

def read_case():
    tokens = raw_input().split()
    pairs = {}
    C = int(tokens[0])
    for i in xrange(1, C + 1):
        bases = elem_pair(tokens[i][:2])
        pairs[bases] = tokens[i][2]
    opposed = dict(zip('QWERASDF', map(lambda _: set(), xrange(8))))
    D = int(tokens[C + 1])
    for i in xrange(C + 2, C + D + 2):
        e1, e2 = tokens[i]
        opposed[e1].add(e2)
        opposed[e2].add(e1)
    return (pairs, opposed, tokens[C + D + 3])

def isbase(el):
    return el in 'QWERASDF'

def solve((pairs, opposed, elements)):
    current = []
    bases = {}
    for e in elements:
        comb = pairs.get(elem_pair((current[-1], e))) if current else None
        if comb:
            cnt = bases[current[-1]] - 1
            if cnt == 0:
                del bases[current[-1]]
            else:
                bases[current[-1]] = cnt
            current[-1] = comb
        elif opposed.get(e, set()) & set(bases):
            current[:] = []
            bases = {}
        else:
            current.append(e)
            if isbase(e):
                bases[e] = bases.get(e, 0) + 1
    return current

T = int(raw_input())
for casenum in xrange(1, T+1):
    result = solve(read_case())
    print("Case #{}: [".format(casenum), end = '')
    print(*result, sep = ', ', end="]\n")
