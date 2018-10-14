#!/usr/bin/env python3
# coding=utf-8

"""
    Solve Quals 2017 p.A

    Author: killerrex
"""

import sys


def is_tidy(n):
    """
    A number is tidy iff:
        n=sum(a_i*10_i, i=0..m)
        a_i >= a_(i+1)
    
    :param n: 
    :return: 
    """

    # To any tidy number you can add a 9 at the end...
    ap = 9
    while n > 0:
        n, a = divmod(n, 10)
        if a > ap:
            return False
        ap = a
    return True


def brute_force(n):

    for m in range(n, 0, -1):
        if is_tidy(m):
            return m
    # A the end, return 0
    # although this si not possible except for n=0
    return 0


def tidylook(n):
    """
    
    :param n: 
    :return: 
    """

    # Fast exit to guarantee that s is at least 2 chars
    if n < 10:
        return n

    s = str(n)
    m = len(s)
    # Search first for the leftmost k such that s[k] > s[k+1]
    # equivalent to a_(m-k) < a_(m-k+1)
    k = 1
    while k < m:
        if s[k-1] > s[k]:
            break
        k += 1
    else:
        # the number is itself tidy
        return n

    # Go back any space of equal numbers as when subtracting they
    # roll and make the result untidy
    while k > 1 and s[k-1] == s[k-2]:
        k -= 1

    # Finally! remove the uglyness
    ugly = int(s[k:]) + 1
    return n - ugly


def check(top):
    for n in range(top):
        a = tidylook(n)
        b = brute_force(n)
        if a != b:
            print("Failure {} => {} {}".format(n, a, b))
    print("Ok")


def solve(fd):
    total = int(fd.readline().strip())

    for j in range(total):
        n = int(fd.readline().strip())

        t = tidylook(n)
        print("Case #{}: {}".format(j+1, t))


def start():
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as fd:
            solve(fd)
    else:
        solve(sys.stdin)


if __name__ == '__main__':
    # check(10000)
    start()
