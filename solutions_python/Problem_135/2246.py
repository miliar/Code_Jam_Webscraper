#!/usr/bin/env python

import sys

def solve_case(n, rowa, grida, rowb, gridb):
    solution = 'unknown'
    a = grida[rowa-1]
    b = gridb[rowb-1]
    match = filter(lambda x: x in b, a)
    if len(match) == 1:
        solution = match[0]
    elif len(match) == 0:
        solution = 'Volunteer cheated!'
    else:
        solution = 'Bad magician!'
    print 'Case #%d: %s' % (n, solution)

with open(sys.argv[1], 'r') as f:
    num_cases = int(f.readline())
    for case in range(num_cases):
        rowa = int(f.readline())
        grida = []
        for i in range(4):
            grida.append(map(int, f.readline().split()))

        rowb = int(f.readline())
        gridb = []
        for i in range(4):
            gridb.append(map(int, f.readline().split()))
        solve_case(case + 1, rowa, grida, rowb, gridb)
