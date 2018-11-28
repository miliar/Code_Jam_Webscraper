#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def solve(shies):
    people = 0
    invites = 0
    for i, v in enumerate(map(int, shies)):
        if i > people:
            needed = i - people
            invites += needed
            people += needed
        people += v
    return invites


def main():
    f = open('A-large.in')
    cases = int(f.readline().strip())
    for case in xrange(cases):
        print 'Case #%d: %d' % (case + 1, solve(f.readline().strip().split(' ')[1]))
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main())
