#!/usr/bin/env python
import sys, operator

def main(argv=None):
    if argv is None:
        argv = sys.argv
    
    T = int(sys.stdin.readline())
    for t in xrange(T):
        N = int(sys.stdin.readline())
        C = map(int, sys.stdin.readline().split(" "))
        x = 0
        sum = 0
        smallest = C[0]
        for c in C:
            x = operator.xor(x, c)
            sum += c
            if c < smallest:
                smallest = c
        if x != 0:
            print "Case #%d: NO" % (t + 1)
        else:
            print "Case #%d: %d" % (t + 1, sum - smallest)

if __name__ == "__main__":
    sys.exit(main())
