#!/usr/bin/env python

import sys
import math


C = int(sys.stdin.readline())
for xxx in xrange(C):
    l = [x for x in sys.stdin.readline().split()]
    ncomb = int(l[0])
    comb = {}
    for i in xrange(ncomb):
        a = l[i+1][0]
        b = l[i+1][1]
        r = l[i+1][2]
        comb[(a, b)] = r
        comb[(b, a)] = r
    ndelete = int(l[ncomb+1])
    delete = set()
    for i in xrange(ndelete):
        a = l[ncomb+i+2][0]
        b = l[ncomb+i+2][1]
        delete.add((a, b))
        delete.add((b, a))
    s = l[-1]
    lista = []
    def check_comb(s):
        while len(s) >= 2:
            if (s[-1],s[-2]) in comb:
                s = s[:-2] + comb[(s[-1],s[-2])]
            else:
                break
        return s

    t = ""
    for c in s:
        t += c
        t = check_comb(t)
        last = t[-1]
        for d in t:
            if (d, t[-1]) in delete:
                t = ""
                break

    print "Case #" + str(xxx+1) + ":",
    if t == "":
        print "[]"
    elif len(t) == 1:
        print "[%s]" % t
    else:
        print "[%s," % t[0],
        for i in t[1:-1]:
            print "%s," % i,
        print "%s]" % t[-1]



