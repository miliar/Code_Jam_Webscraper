#!/usr/bin/env python2.6
# -*- Mode: python; indent-tabs-mode: nil; py-indent-offset: 4; python-indent: 4; -*-
# vim:expandtab softtabstop=4 shiftwidth=4:
from __future__ import division
import sys

def Foo(L, P, C):
    x = P/L
    n = 0
    #print P, L, x
    f = C
    while L*f < P:
        f = f*f
        n += 1
        #print x, n
    return n
def main():
    it = iter(sys.stdin)
    T = int(next(it))
    for i in range(T):
        p = map(int, next(it).split())
        print "Case #%d: %s" %(i+1, Foo(*p))

if __name__=="__main__":
    main()
