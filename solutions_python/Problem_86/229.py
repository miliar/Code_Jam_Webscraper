#!/usr/bin/python

import sys
import math
from fractions import gcd



def perfect(n, low, hi):
    if low <= 1:
        return 1
    if hi < low:
        return "NO"
    n.sort()

    l = 1
    lh = []
    mm = []
    for i in range(low, hi+1):
        lh.append(i)
        mm.append(True)
    for x in n:
        for i in range(len(lh)):
            if (x > lh[i]) and (x % lh[i] != 0):
                mm[i] = False
            elif (lh[i] > x) and (lh[i] % x != 0):
                mm[i] = False
    for i in range(len(mm)):
        if mm[i]:
            return lh[i]
    return "NO"


def main(argv=None):
    if argv is None:
        argv = sys.argv
    if not len(argv) == 2:
        print >>sys.stderr, "Usage: store-credit.py infile"

    infile = argv[1]
    f = open(infile, 'r')
    N = int(f.readline())

    for i in range(N):
        n, low, hi = map(lambda x: int(x), f.readline().strip().split())
        arr = map(lambda x: int(x), f.readline().strip().split())
        result = perfect(arr, low, hi)
        print "Case #%d: %s" % (i + 1, result)
        
if __name__ == "__main__":
    sys.exit(main())

