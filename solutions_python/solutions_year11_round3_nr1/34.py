#!/usr/bin/env python2.7
from __future__ import print_function

def read_case():
    rows, cols = (int(s) for s in raw_input().split())
    case = []
    for y in xrange(rows):
        case.append(raw_input())
    return case

def try_tile(case, y, x):
    if len(case) < y+2 or len(case[y]) < x+2:
        return False
    if case[y][x:x+2] != ['#', '#'] or case[y+1][x:x+2] != ['#', '#']:
        return False
    case[y][x:x+2] = ['/', '\\']
    case[y+1][x:x+2] = ['\\', '/']
    return True

def solve(case):
    case = [list(row) for row in case]
    failed = False
    for y, x in ((y,x) for y in xrange(len(case)) \
            for x in xrange(len(case[y]))):
        if case[y][x] == '#' and not try_tile(case, y, x):
            failed = True
            break
    return not failed and case

def print_result(res):
    if not res:
        print("Impossible")
    else:
        for row in res:
            print(''.join(row))

T = int(raw_input())
for caseidx in xrange(1, T+1):
    print("Case #{}:".format(caseidx))
    print_result(solve(read_case()))
