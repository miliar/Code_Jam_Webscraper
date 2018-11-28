#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
http://bit.ly/1O2UcwC
'''

import bisect
import collections
import collections.abc
import itertools
import math
import re
import sys

from pprint import pprint


# ------------------------
# Be creative here
# ------------------------

def readcase(f):
    return readline(f)


WORDS = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
LEVELS = [
    [0, 2, 4, 6, 8],
    [3, 5, 7],
    [1, 9]
]

# unique = ['Z', 'O', 'W', 'H', 'U', 'F', 'X', 'S', 'G', 'I']


def decr(d, w):
    by = min(d[c] for c in w)
    for c in w:
        d[c] -= by
    return by


def hehe():
    d = defdict()
    for w in digits:
        for c in w:
            d[c] += 1
    pprint(d)


def build(s):
    letters = defdict()
    for c in s:
        letters[c] += 1
    return letters


def solve(s):
    d = build(s)
    ary = [0] * 10
    for level in LEVELS:
        for digit in level:
            ary[digit] += decr(d, WORDS[digit])
    ans = []
    for i, x in enumerate(ary):
        ans.append(str(i) * x)
    return strjoin(ans, '')


# ------------------------
# No touchy
# ------------------------

class InputReader(collections.abc.Iterable):

    _cases = None

    def __init__(self, reader, inp=None):
        self._read(reader, inp or sys.stdin)

    def _read(self, reader, inp):
        t = int(next(inp))
        self._cases = [reader(inp) for _ in range(t)]
        assert len(self._cases) == t

    def __iter__(self):
        return iter(self._cases)


def main():
    inp = InputReader(readcase)
    for i, c in enumerate(inp, start=1):
        print('Case #{}: {}'.format(i, solve(c)))


# ------------------------
# Utilities
# ------------------------

def bsearch(a, x):
    '''
    Locate the leftmost value exactly equal to x.
    https://docs.python.org/3/library/bisect.html#module-bisect
    '''
    i = bisect.bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    raise ValueError


def defdict(x=0):
    return collections.defaultdict(lambda: x)


def mapadd(xs, y):
    return [x + y for x in xs]


def readint(f):
    return int(readline(f))


def readints(f, expected=None, sep=None):
    line = readline(f)
    xs = [int(e) for e in line.split(sep)]
    if expected is not None:
        assert len(xs) == expected, '{} != {}'.format(len(xs), expected)
    return xs


def readline(f):
    return next(f).strip()


def rwh_primes2(n):
    '''
    Input n >= 6, returns a list of primes, 2 <= p < n.
    http://stackoverflow.com/revisions/33356284/2
    '''
    # TODO: Silence PEP8's E221 warning.
    zero  = bytearray([0])
    size  = n // 3 + (n % 6 == 2)
    sieve = zero + bytearray([1]) * (size - 1)
    top   = int(math.sqrt(n)) // 3
    for i in range(top + 1):
        if sieve[i]:
            k     = (3*i + 1) | 1
            ksq   = k * k
            k2    = k * 2
            start = (ksq + k2 * (2 - (i & 1))) // 3
            ksqd3 = ksq // 3
            sieve[ksqd3::k2] = zero * ((size - ksqd3 - 1) // k2 + 1)
            sieve[start::k2] = zero * ((size - start - 1) // k2 + 1)
    ans = [2, 3]
    poss = itertools.chain.from_iterable(
        itertools.zip_longest(*[range(i, n, 6) for i in (1, 5)])
    )
    ans.extend(itertools.compress(poss, sieve))
    return ans


def strjoin(xs, glue=' ', conv=str):
    return glue.join(map(conv, xs))


if __name__ == '__main__':
    main()
