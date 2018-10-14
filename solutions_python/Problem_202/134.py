#!/usr/bin/python

import sys

from collections import OrderedDict, Counter
from itertools import chain

def fill_xes(n, xes):
    rows = set(range(n))
    cols = set(range(n))
    for r, c in xes:
        rows.remove(r)
        cols.remove(c)
    assert len(rows) == len(cols)
    return zip(rows, cols)


def d1(r, c):
    return c - r

def d2(r, c):
    return r + c


def fill_pluses(n, pluses):
    d1s = set(d1(r, c) for r, c in pluses)
    d2s = set(d2(r, c) for r, c in pluses)

    cells = []

    for r, c in chain(
        ((0, c) for c in xrange(n)),
        ((n-1, c) for c in xrange(n)),
        ((r, 0) for r in xrange(n)),
        ((r, n-1) for r in xrange(n))
    ):
        if d1(r, c) not in d1s and d2(r, c) not in d2s:
            d1s.add(d1(r, c))
            d2s.add(d2(r, c))
            cells.append((r, c))

    return cells


def solve(n, models):
    xes = {(r, c) for t, r, c in models if t in ('x', 'o')}
    pluses = {(r, c) for t, r, c in models if t in ('+', 'o')}
    
    xes |= set(fill_xes(n, xes))
    pluses |= set(fill_pluses(n, pluses))
    
    updated_models = (
        {('x', r, c) for r, c in (xes - pluses)}
        | {('+', r, c) for r, c in (pluses - xes)}
        | {('o', r, c) for r, c in (pluses & xes)}
    )

    return len(xes) + len(pluses), updated_models


def prn(n, models):
    stage = [['.']*n for i in xrange(n)]
    models = {(r, c):t for t, r, c in models}
    for r in xrange(n):
        for c in xrange(n):
            stage[r][c] = models.get((r, c), '.')
    for row in stage:
        print "".join(row)


def main():
    T = int(next(sys.stdin))
    for test in xrange(1, T+1):
        n, m = (int(x) for x in next(sys.stdin).split())
        models = set()
        for i in xrange(m):
            t, r, c = next(sys.stdin).split()
            models.add((t, int(r) - 1, int(c) - 1))
        style_points, updated_models = solve(n, models)
        updates = updated_models - models
        print "Case #{}: {} {}".format(test, style_points, len(updates))
        for t, r, c in updates:
            print t, r+1, c+1
#        print; prn(n, models); print; prn(n, updated_models); print


main()

