#!/usr/bin/env python

import sys
fin = sys.stdin

def main():
    T = int(fin.readline())
    for t in xrange(T):
        N, K = map(int, fin.readline().split())
        ok = True
        while N >= 1:
            if K % 2 == 0:
                ok = False
            K /= 2
            N -= 1
        print "Case #%d: %s" % (t + 1, "ON" if ok else "OFF")
    return 0

if __name__ == "__main__":
    main()

