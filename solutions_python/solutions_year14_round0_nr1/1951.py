#!/usr/bin/python

from __future__ import print_function
import sys
from collections import namedtuple

Case = namedtuple('Case', 'ans cards')

def main():
    T = int(next(sys.stdin))
    for x in range(1, T+1):
        cases = []
        for case_n in range(2):
            cases.append(Case(
                ans = int(next(sys.stdin)) - 1,
                cards = [next(sys.stdin).split() for row in range(4)],
            ))

        isect = set(cases[0].cards[cases[0].ans]).intersection(cases[1].cards[cases[1].ans])
        if len(isect) == 1:
            print("Case #{}: {}".format(x, isect.pop()))
        elif len(isect) == 0:
            print("Case #{}: Volunteer cheated!".format(x))
        else:
            print("Case #{}: Bad magician!".format(x))

if __name__ == '__main__':
    main()

