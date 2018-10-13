#!/usr/bin/python

from __future__ import division
from __future__ import print_function

import itertools
import sys

def solve(line):
    line = iter(line.split())
    next(line)
    # make bases
    bases = {}
    for s in line:
        if s.isdigit():
            break
        bases[frozenset(s[:2])] = s[2:]
    # make oppositions
    opps = set()
    for s in line:
        if s.isdigit():
            break
        opps.add(frozenset(s))
    # make invocation
    invokes = next(line)
    # quick assertion
    for s in line:
        assert False
    stack = []
    for char in invokes:
        if stack:
            newchar = bases.get(frozenset((stack[-1],char)))
            if newchar is not None:
                stack[-1] = newchar
                continue
        for i,s in enumerate(stack):
            if frozenset((s,char)) in opps:
                del stack[:]
                break
        else:
            stack.append(char)
    return repr(stack).replace("'", "")


def main(filename):
    with open(filename, "r") as f:
        for case, line in enumerate(f):
            if not case:
                T = int(line.strip())
                continue
            if case > T:
                break
            print("Case #{0}: {1}".format(case, solve(line)))


if __name__ == "__main__":
    main(sys.argv[1])
    sys.exit(0)

