#!/usr/bin/env python3
# coding=utf-8

"""
    Solve Quals 2017 p.A

    Author: killerrex
"""


import sys


class Gap(tuple):
    """
    Urinary goes from k=0 to k=n-1
    
    left = k
    right = n - (k+1)
    
    n = 2m + r
    Chosen one is always:
        t = (n-1) // 2 = m + r - 1
        L_t = t = m + r - 1
        R_t = n - (t + 1) = 2m + r - (m + r - 1 + 1) = m
    """
    def __new__(cls, n):
        m, r = divmod(n, 2)
        left = m + r - 1
        right = m
        return super(Gap, cls).__new__(cls, (left, right, n))

    @property
    def left(self):
        return self[0]

    @property
    def right(self):
        return self[1]

    @property
    def n(self):
        return self[2]

    def split(self):
        return [Gap(v) for v in self[:2] if v > 0]


def brute(n, k):

    choose = Gap(n)
    lavatory = [choose]
    for j in range(k):
        # Get the biggest one and split it
        choose = lavatory[-1]
        lavatory = lavatory[:-1] + choose.split()
        lavatory.sort()
    # Last chosen one are the result
    return choose.left, choose.right


def staller(n, k):
    """
    """

    # Isolate the last one...
    k -= 1

    # First try to perform "full" divisions
    dg = 1
    g = 0
    while k >= dg:
        # Ok, still margin to spend...
        k -= dg
        g += dg
        # Next step
        dg *= 2

    # Ok, reduce n accordingly
    a, xtra = divmod(n-g, g+1)

    # Now we have r gaps of a+1 and g+1-r gaps of a
    # to put the last k elements
    # And let the last one choose place
    k += 1
    if k > xtra:
        # Last selected is an "a" gap
        last = a
    else:
        last = a + 1

    # In a gap of size a = 2*m + r
    # left = m + r - 1 and right = m
    m, r = divmod(last, 2)
    return m + r - 1, m


def check(nmax):

    print("Check n, k => brute, direct")
    for n in range(1, nmax):
        for k in range(1, n+1):
            b = brute(n, k)
            g = staller(n, k)
            if b != g:
                print("Fail {}, {} => {} != {}".format(n, k, b, g))
    print("End check")


def solve(fd):
    total = int(fd.readline().strip())

    for j in range(total):
        n, k = [int(v) for v in fd.readline().split()]
        left, right = staller(n, k)
        print("Case #{}: {} {}".format(j + 1, right, left))


def start():
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as fd:
            solve(fd)
    else:
        solve(sys.stdin)

if __name__ == '__main__':
    # check(200)
    start()
