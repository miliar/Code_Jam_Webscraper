#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sys

debug = False

def print_debug(line):
    if debug:
        print line

def solve(D, N, KS):
    t_max = 0.0
    s_max = 0.0
    for k,s in KS:
        ti = float(D-k)/s
        if ti > t_max:
            t_max = ti
            s_max = D/ti
            
    return s_max

if '-D' in sys.argv:
    debug = True

T = int(raw_input())

for test_case in range(1, T+1):
    D,N = [int(s) for s in raw_input().split(" ")]
    KS = []
    for i in xrange(N):
        K,S = [int(s) for s in raw_input().split(" ")]
        KS.append((K,S))
    
    
    solution = solve(D, N, sorted(KS))
    print "Case #{}: {}".format(test_case, solution)

