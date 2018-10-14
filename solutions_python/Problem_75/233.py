#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
http://code.google.com/codejam/contest/dashboard?c=975485#s=p1
'''

import sys, re, math

def lin(): return sys.stdin.readline()
def ints(): return [int(s) for s in lin().split()]

ncases = ints()[0]
for casenum in range(ncases):
    ls = lin().split()
    C = int(ls[0])
    cs = {}
    for i in range(1,C+1):
        s = ls[i]
        cs[(s[0],s[1])]=s[2]
        cs[(s[1],s[0])]=s[2]
    D = int(ls[C+1])
    ds = {}
    for i in range(1, D+1):
        s = ls[C+1+i]
        ds[s[0]]=s[1]
        ds[s[1]]=s[0]
    N = int(ls[C+1+D+1])
    inp = ls[C+1+D+2]
    s = []
    for c in inp:
        if len(s) and cs.has_key((c,s[-1])):
            s[-1] = cs[(c,s[-1])]
        elif len(s) and ds.has_key(c) and ds[c] in s:
            s = []
        else:
            s += c

    print "Case #%d: %s" % (casenum+1, str(s).replace("'",""))#'[' + (', '.join('%c'%c) for c in s) + ']')
