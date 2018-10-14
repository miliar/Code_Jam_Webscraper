#!/usr/bin/env python2.6
# -*- Mode: python; indent-tabs-mode: nil; py-indent-offset: 4; python-indent: 4; -*-
# vim:expandtab softtabstop=4 shiftwidth=4:
import sys

def Num(N, e):
    e.sort()
    c = 0
    for i in range(len(e)-1):
        a,b = e[i]
        c += sum(1 for ap,bp in e[i+1:] if bp < b)
    return c
def main():
    it = iter(sys.stdin)
    T = int(next(it))
    for t in range(T):
        N, = map(int, next(it).split())
        e = list()
        for i in range(N):
            A, B = map(int, next(it).split())
            e.append((A, B))
        assert N == len(e)
        print "Case #%d: %s" %(t+1, Num(N, e))

if __name__=="__main__":
    main()
