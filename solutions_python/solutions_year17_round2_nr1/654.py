#!/usr/bin/python
from decimal import *

getcontext().prec = 12

def main():
    T = int(raw_input())
    for i in xrange(T):
        d, n = raw_input().split()
        d = Decimal(d)
        n = int(n)
        Vmax = Decimal("0.")
        for j in xrange(n):
            k, m = map(Decimal, raw_input().split())
            v = (d - k) / m
            if Vmax < v:
                Vmax = v

        print "Case #%d: %s" % (
            i + 1,
            "{0:f}".format(d / Vmax),
        )
        
if __name__ == "__main__":
    main()
