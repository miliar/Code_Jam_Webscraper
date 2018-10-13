#!/usr/bin/env python
# -*- coding: utf-8 -*-
import fileinput

cons = list("bcdfghjklmnpqrstvwxyz")
vow = list("aeiou")

def read(fin):
        s,n = fin.readline().split()
        n = int(n)
        return s,n

def check(s,n):
        l = len(s)
        for i in range(l-n+1):
                res = True
                for p in range(n):
                        if s[i+p] in vow:
                                res = False
                                break
                if res:
                        return True
        return False

def solve(s,n):
        l = len(s)
        nvalue = 0
        for i in range(l-n+1):
                for j in range(i+n,l+1):
                        if check(s[i:j],n):
                                nvalue += 1
        return nvalue


fin=fileinput.input()
T = int(fin.readline())

#import pdb
#pdb.set_trace()
for i in range(T):
        s,n = read(fin)
        print "Case #%d: %d" % (i+1,solve(s,n))
