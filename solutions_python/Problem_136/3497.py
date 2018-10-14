#!/usr/bin/env python


import sys


def solve(C, F, X):
    t = X / 2.0
    b = 1
    while True:
        t1 = sum(C / (2.0 + B * F) for B in xrange(b)) + X / (2.0 + b * F)
        if t1 < t:
            t = t1
        else:
            break
        b += 1
    return t


def main():
    with open(sys.argv[1], 'r') as fin:
        T = int(fin.readline().strip())
        for t in xrange(T):
            C, F, X = map(float, fin.readline().strip().split(" "))
            print "Case #%d: " % (t + 1),
            print "%.7f" % solve(C, F, X)
            print


if __name__ == '__main__':
    main()

