#!/usr/bin/env python

import sys
from collections import namedtuple

group = namedtuple('group', ['v', 'west', 'east', 'westp', 'eastp', 't'])

def readline():
    return sys.stdin.readline().rstrip('\r\n')


def testcase():
    C, D = map(int, readline().split())
    D = float(D)

    def readgroup():
        p, v = map(int, readline().split())
        t = float((v-1) * D) / 2
        return group(v=v, west=p-t, east=p+t, westp=p, eastp=p, t=t)

    def merge(g1, g2):
        v = g1.v + g2.v
        westp = min(g1.westp, g2.westp)
        eastp = max(g1.eastp, g2.eastp)
        mint = (D*(v-1) - (eastp - westp)) / 2
        west = westp-mint
        east = eastp+mint
        t = max(mint, g1.t, g2.t)
        result = group(v=v, west=west, east=east, westp=westp, eastp=eastp, t=t)
        return result

    vendors = [readgroup() for i in range(C)]
    vendors.sort(key=lambda g: g.east)

    again = True
    while again:
        again = False
        for i in range(len(vendors)-1):
            g1, g2 = vendors[i], vendors[i+1]
            if not (g2.west - g1.east >= D or g1.west - g2.east >= D):
                vendors = vendors[:i] + [merge(g1, g2)] + vendors[i+2:]
                again = True
                break

    return max(g.t for g in vendors)


def main():
    n_cases = int(readline())
    for t_case in xrange(1, n_cases+1):
        print "Case #%d: %.1f" % (t_case, testcase())

if __name__ == '__main__':
    main()
