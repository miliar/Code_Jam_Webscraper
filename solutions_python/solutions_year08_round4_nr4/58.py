#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Google CodeJam

Solution by Joao Moreno <alph.pt@gmail.com> 2008

Usage: python [source_file] < [input_file] > [output_file]
"""

def all_perms(l):
    if len(l) <= 1:
        yield l
    else:
        for perm in all_perms(l[1:]):
            for i in range(len(perm)+1):
                yield perm[:i] + l[0:1] + perm[i:]

def size(str):
    if len(str) == 1:
        return 1
    
    s = 1
    prev = str[0]
    for p in str[1:]:
        if prev != p:
            s += 1
        prev = p
    
    return s

from codejam.io import Scanner
s = Scanner()
N = s.readInt()
for i in range(1,N+1):
    K = s.readInt()
    S = s.readLine()
    r = None
    for arr in all_perms(range(K)):
        nS = ""
        p = 0
        for j in range(len(S)/K):
            for a in arr:
                nS += S[p+a]
            p += K
        b = size(nS)
        if r is None or r > b:
            r = b
    print "Case #%i: %i" % (i,r)