#!/usr/bin/env python

def solve():
    n = int(raw_input())
    inputs = []
    for i in xrange(n):
        print 'Case #%d: %d' % (i + 1, solve_single())

def solve_single():
    line = raw_input()
    max_str, ns_str = line.split(' ')
    max_shy = int(max_str)
    clapping = 0
    level = 0
    result = 0
    for n_str in ns_str:
        n_shy = int(n_str)
        needed = level - clapping
        if needed > 0:
            result += needed
            clapping += needed
        clapping += n_shy
        level += 1
    return result


if __name__ == '__main__':
    solve()
