#!/usr/bin/env python

import re
import itertools


def substrings(n):
    return (n[r] for r in itertools.starmap(slice, itertools.combinations(range(len(n)+1), 2)))


def hasconsonants(n):
    v = re.compile(r'[^aeiou]{%s}' % n)

    def _f(name):
        return bool(v.search(name))
    return _f


def solve(fin):
    name, n = next(fin).split()
    n = int(n)
    return sum(map(hasconsonants(n), substrings(name)))

if __name__ == '__main__':
    fn = 'A-small-attempt0'
    fin = open(fn + '.in')
    fout = open(fn + '.out', 'w')
    T = int(next(fin))
    for i in range(1, T + 1):
        print("Case #{}:".format(i), solve(fin), file=fout)
