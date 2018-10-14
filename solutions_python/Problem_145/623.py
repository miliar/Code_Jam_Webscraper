#!/usr/bin/env python

import sys
import math
from fractions import gcd


def main():
    T = int(sys.stdin.readline().strip())
    for case_id in range(1, T+1):
        p, q = map(int, sys.stdin.readline().strip().split('/'))
        g = gcd(p, q)
        p /= g
        q /= g
        o = math.log(q, 2)
        if int(o) != o:
            print "Case #" + str(case_id) + ": impossible"
        elif p == 1:
            print "Case #" + str(case_id) + ": " + str(int(o))
        else:
            #pp = p * 2 - q
            #if pp > 0:
            x = int(math.log(p, 2))
            r = int(o) - x
            print "Case #" + str(case_id) + ": " + str(r)
            #else:
                #print "Case #" + str(case_id) + ": impossible"

if __name__ == '__main__':
    main()
