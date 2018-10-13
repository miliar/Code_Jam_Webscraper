#!/usr/bin/python -tt

import sys


def cookie_click(C, F, X, N_farms=0.0, t=0.0, tmax = float('inf')):

    # Time till we get all cookies
    t1 = t + (X / (2.0 + F * N_farms))

    if t1 > tmax:
        return tmax
    else:
        tmax = t1

    # Time till we can buy a farm
    t += C / (2.0 + F * N_farms)

    t2 = cookie_click(C, F, X, N_farms+1.0, t, tmax)

    if t2 >= t1:
        return t1

    return t2


def main():
    sys.setrecursionlimit(10000)
    n_cases = int(sys.stdin.readline())

    for case in xrange(n_cases):
        [C, F, X] = map(float, sys.stdin.readline().split())

        res = cookie_click(C, F, X)
        print 'Case #%d: %.7f' % (case+1, res)


if __name__ == '__main__':
    main()
