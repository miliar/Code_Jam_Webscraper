#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys
rdl = sys.stdin.readline


def process(case):
    """precessing case #"""
    r, k, n = (int(i) for i in rdl().split())
    g = list((int(i) for i in rdl().split()))
    income = 0
    for dumb in xrange(r):
        this_run = []
        tot = 0
        while len(g)>0 and tot+g[0] <= k:
            next = g.pop(0)
            tot += next
            this_run.append(next)
        income += tot
        g += this_run
        #print "this run:", this_run
    return income
        
        
    

cases = int(rdl())
for case in xrange(1, cases+1):
    print "Case #%d:"%case, process(case)
