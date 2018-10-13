#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys
import bisect

get_ints = lambda f:map(int, next(f).strip().split(' '))

def b(N, i):
    if i == 2 ** N - 1 or i == 0:
        return i
    else:
        return b(N-1, (i + 1) / 2)

def w(N, i):
    if i == 2 ** N - 1 or i == 0:
        return i
    else:
        return 2 ** (N -1) + w(N -1, (i - 1) / 2)

def f(N, P):
    i = j = 0
    k = 2 ** (N -1)
    while k >=1:
        if b(N, i + k) < P:
            i += k
        if w(N, j + k) < P:
            j += k
        k = k/2
    return j, i

def get_input(f):
    T = int(next(f))
    for _ in range(T):
        N, P = get_ints(f)
        yield N, P

def main():
    for i, Input in enumerate(get_input(sys.stdin)):
        y, z = f(*Input)
        print "Case #{0}: {1} {2}".format(i + 1, y, z)

if __name__ == "__main__":
    main()
