#!/usr/bin/env python

from __future__ import print_function, division
__metaclass__ = type

import sys, re

def run(filename):
    words = []
    cases = []

    with open(filename) as f:
        L, D, N = map(int, f.readline().strip().split())
        for line in f:
            words.append(line.strip())
            if len(words) >= D:
                break
        for line in f:
            cases.append(line.strip())
            if len(cases) >= N:
                break

    for i, case in enumerate(cases):
        case = case.replace('(','[').replace(')',']')
        r = re.compile(case)
        matches = sum(1 for x in words if r.match(x))
        print('Case #{0}: {1}'.format(i+1, matches))


if __name__ == "__main__":
    try:
        filename, = sys.argv[1:]
    except ValueError:
        print('USAGE: %s filename'%sys.argv[0], file=sys.stderr)
        sys.exit(1)
    run(filename)
