#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
http://code.google.com/codejam/contest/dashboard?c=975485#
'''

import sys, re, math

def lin(): return sys.stdin.readline()
def ints(): return [int(s) for s in lin().split()]
def sgn(x): return 1 if x>0 else -1 if x<0 else 0

ncases = ints()[0]
for casenum in range(ncases):
    ls = lin().split()
    N = int(ls[0])
    ws = []; bs = []; os = []
    for i in range(1,N+1):
        C = ls[2*i-1]
        w = int(ls[2*i])
        ws.append((C,w))
        if C == 'O': os.append(w)
        elif C=='B': bs.append(w)
        else: assert False, '%s must be either O or B' % C
        
    T = 0; op = 1; bp = 1
    while ws:
        T += 1
        if ws[0]==('O', op):
            ws = ws[1:]
            os = os[1:]
            if len(bs): bp += sgn(bs[0]-bp)
        elif ws[0] == ('B', bp):
            ws = ws[1:]
            bs = bs[1:]
            if len(os): op += sgn(os[0]-op)
        else:
            if len(os): op += sgn(os[0]-op)
            if len(bs): bp += sgn(bs[0]-bp)

    print "Case #%d: %d" % (casenum+1, T)
