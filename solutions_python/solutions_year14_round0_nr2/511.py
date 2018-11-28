#!/usr/bin/env python

import sys


def main():
    T = int(sys.stdin.readline())
    for i in range(1, T+1):
        C, F, X = map(float, sys.stdin.readline().strip().split())
        r = 2.0
        if X <= C:
            t = X / r
        else:
            cookie = C
            t = C / r
            while cookie < X:
                t1 = (X - cookie + C) / (r + F)
                t2 = (X - cookie) / r
                if t1 < t2:
                    r += F
                    t += C / r
                else:
                    t += t2
                    cookie = X
        print "Case #" + str(i) + ": " + str(t)


if __name__ == '__main__':
    main()
