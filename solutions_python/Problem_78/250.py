#! /usr/bin/env python
# -*- coding:utf-8 -*-
import sys

sys.setrecursionlimit(1100)
#sys.maxint
#-sys.maxint-1

def findG(wd, d, pg):
    if d-wd > 0 and pg == 100:
        return False
    if wd > 0 and pg == 0:
        return False
    g = d
    while g <= sys.maxint:
        wg = g*pg
        if wg%100 == 0:
            wg /= 100
            #print "wg %d, g %d for d %d (g-wg %d, d-wd %d)" % (wg, g, d, g-wg, d-wd)
            if wg >= wd and g-wg >= d-wd:
                return True
        g = g + 1
    return False

def doIt(n, pd, pg):
    for d in range(1,n+1):
        wd = d*pd
        if wd%100 == 0:
            # possible
            wd /= 100
            if findG(wd, d, pg):
                return True
    return False

if __name__ == '__main__':
    f = open(sys.argv[1])

    num_of_case = int(f.readline())
    for i in range(num_of_case):
        #n = int(f.readline())
        params = map(int, f.readline().split())

        n = params[0]
        pd = params[1]
        pg = params[2]
        answer = doIt(n, pd, pg)
        print "Case #%d: %s" % (i+1, "Possible" if answer else "Broken")

