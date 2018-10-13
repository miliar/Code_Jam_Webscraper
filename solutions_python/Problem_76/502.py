""" Welcome to Code Jam

:Abstract: Solution to Google Code Jam 2011 qualification
:Authors:  iki
:Contact:  jan.killian at (g)mail.com

.. contents::

Problem statement
=================

Input
-----

Output
------

Limits
------

Doctest
=======

>>> p = lambda x,y: (x | y) - (x & y)
>>> p(5, 4)
1
>>> p(7, 9)
14
>>> p(50, 10)
56


>>> test(
...   testlabel='sample',
...   testinput='''2
... 5
... 1 2 3 4 5
... 3
... 3 5 6
... ''')  #doctest: +NORMALIZE_WHITESPACE
Case #1: NO
Case #2: 11
"""
__docformat__ = 'restructuredtext en'

from codejam import *

def solve(values):
    M = max(values)
    b = 1
    mask = 0
    bits = {}
    while b < M:
        s = sum(i & b for i in values)

        if s:
            bits[b] = s = s / b
            mask |= b

            if log.debug: log.debug([b, s])

            if s & 1:
                return 0

        b *= 2

    if not mask:
        return 0

    return find(sorted(values), ~mask)

def find(values, mask, select=0, bits=0, next=0, add=None):
    if add is not None:
        select += add
        bits = (bits | add) - (bits & add)
        if select & mask == 0:
            return sum(values) - select

    v = len(values)
    while next < v:
        f = find(values, mask, select, bits, next + 1, values[next])
        if f:
            return f
        next += 1

    return 0

def parse(fi):
    N = int(fi.next())
    values = map(int, fi.next().split())
    assert N == len(values), (N, len(values))
    return values,

def format(r):
    return r or 'NO'

if __name__ == '__main__':
    main(solve, parse, format)
