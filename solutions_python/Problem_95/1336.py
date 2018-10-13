#!/usr/bin/env python
import sys


class Case(object):
    MAP = {'q': 'z', 'z': 'q', ' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm'}
    def __init__(self, *letters):
        self.letters = letters

    @classmethod
    def parse(cls, f):
        letters = f.readline().strip()

        return Case(*letters)

    def solve(self):
        return ''.join(self.MAP[c] for c in self.letters)


def parse(f):
    case_count = int(f.readline().strip())
    cases = []

    for i in range(case_count):
        cases.append(Case.parse(f))

    results = [c.solve() for c in cases]

    for i, s in enumerate(results, start=1):
        print 'Case #%d: %s' % (i, s)


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        parse(f)
