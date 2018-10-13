#!/usr/bin/env python3
# coding=utf-8

"""
  Solution to Qualification Round.A

  Author: killerrex@gmail.com
"""

import sys
import collections

from itertools import accumulate, product
from functools import reduce
import operator

# Get the primes in a direct way, we do not need more than 1000
_primes = [2, 3]


def fill_primes(lim):
    """
    Add primes until lim is reached
    :param lim:
    """
    p = _primes[-1]
    while p < lim:
        p += 2
        for d in _primes:
            if p % d == 0:
                break
        else:
            _primes.append(p)


def factored(n):
    """
    Extract the prime factors
    :param n: number
    :return: [ (pi, muli) ]
    """

    pset = []
    mset = []
    k = 0
    while n > 1:
        # We work with small numbers... _primes is filled enough
        p = _primes[k]
        c, r = divmod(n, p)
        if r != 0:
            k += 1
            continue
        n = c
        if p in pset:
            mset[-1] += 1
        else:
            pset.append(p)
            mset.append(1)
    return zip(pset, mset)


_divcache = {}


def divisors(n):
    """
    Return the ordered set of proper divisors
    (not including (1,n) and (n,1)
    :param n: Number to split
    :return: [ (a,b) ] con a,b = n
    """

    if n in _divcache:
        return _divcache[n]

    # first factorize
    fac = factored(n)

    # Vary each exponent from 0 to alpha_i
    factors = []
    for p, m in fac:
        s = [1] + [p]*m
        col = list(accumulate(s, operator.mul))
        factors.append(col)

    # Now create all the possible products, in a nice order
    factors.reverse()
    div = [reduce(operator.mul, cmb) for cmb in product(*factors)]

    # Remove the (1, n) and (n, 1)
    _divcache[n] = div[1:-1]
    return _divcache[n]


_bcache = {}


def brute(state):
    """
    Solve by brute force...
    :param state:
    :return:
    """

    if not state:
        return 0

    key = tuple(state)

    if key in _bcache:
        return _bcache[key]

    # Try to divide the max
    p, m = state[-1]

    if p <= 3:
        _bcache[key] = p
        return p

    # Base solution, just let the people eat 1 round
    # This is a prime number...just let eat 1 round
    new = [(pi-1, mi) for pi, mi in state if pi > 1]
    best = 1 + brute(new)

    # Try each divisor
    # Upper limit, just do nothing
    div = divisors(p)
    for b in div:
        # Divide each p in b parts of a elements
        a = p // b
        new = sorted(state[:-1] + [(a, m * b)])
        t = m * (b - 1) + brute(new)
        best = min(best, t)

    _bcache[key] = best
    return best


def solve(fd):
    """
    Solve the input
    :param fd: stdin
    """

    cases = int(fd.readline().strip())

    for k in range(cases):
        txt = fd.readline().strip()
        if not txt:
            continue

        d = int(txt)

        pancakes = [int(c) for c in fd.readline().strip().split()]

        assert(len(pancakes) == d)
        pancakes.sort()

        # Count! dracula
        cnt = collections.Counter(pancakes)
        state = sorted(cnt.items())

        steps = brute(state)
        print("Case #{}: {}".format(k+1, steps))


if __name__ == '__main__':
    # According to the definition Pi <=1000
    fill_primes(1001)

    # Read stdin and write stdout
    solve(sys.stdin)
