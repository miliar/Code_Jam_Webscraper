#!/usr/bin/env python

import sys, operator
from itertools import count

class memoizing(object):

    def __init__(self, function):
        self.function = function
        self.memoized = {}
        self.tried = set()

    def __call__(self, *args):
        try:
            return self.memoized[args]
        except KeyError:
            if args in self.tried:
                return False
            self.tried.add(args)
            self.memoized[args] = self.function(*args)
            return self.memoized[args]


@memoizing
def ishappy(number, base):
    if number == 1:
        return True
    s = 0
    while number:
        number, digit = divmod(number, base)
        s += digit * digit
    return ishappy(s, base)


no_cases = input()
lines = []

for line in sys.stdin:
    lines.append(frozenset(int(b) for b in line.split()))

unsolved_lines = set(lines)
solved_lines = {}

all_bases = reduce(operator.or_, lines)

for no in count(2):
    this_happies = set()
    for base in all_bases:
        if ishappy(no, base):
            this_happies.add(base)
    for unsolved in list(unsolved_lines):
        if unsolved <= this_happies:
            all_bases = reduce(operator.or_, unsolved_lines)
            unsolved_lines.remove(unsolved)
            solved_lines[unsolved] = no
    if not unsolved_lines:
        break

for no, line in enumerate(lines):
    print "Case #%d: %d" % (no + 1, solved_lines[line])
