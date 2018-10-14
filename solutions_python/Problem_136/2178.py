#!/usr/bin/env python

import sys

def should_buy_farm(secs, cps, C, F, X):
    "meat of the matter..."
    farmtime = time_to_farm(secs, cps, C, F, X)
    return farmtime + time_to_win(secs, cps + F, C, F, X) < time_to_win(secs, cps, C, F, X)

def time_to_farm(secs, cps, C, F, X):
    return C / cps

def time_to_win(secs, cps, C, F, X):
    return secs + (X / cps)

def solve_case(n, C, F, X):
    secs = 0.0
    cps = 2.0                   # cookies per second

    while should_buy_farm(secs, cps, C, F, X):
        secs += time_to_farm(secs, cps, C, F, X)
        cps += F
    secs = time_to_win(secs, cps, C, F, X)

    print 'Case #%d: %0.7f' % (n, secs)

with open(sys.argv[1], 'r') as f:
    num_cases = int(f.readline())
    for case in range(num_cases):
        C, F, X = map(float, f.readline().split())
        solve_case(case + 1, C, F, X)
