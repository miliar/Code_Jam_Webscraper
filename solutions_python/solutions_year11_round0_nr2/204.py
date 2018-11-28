#! /usr/bin/env python
import sys

def main():
    t = int(raw_input())
    for i in xrange(t):
        line = raw_input().split()
        c, line = int(line[0]), line[1:]
        compounds, line = line[:c], line[c:]
        d, line = int(line[0]), line[1:]
        opposites, line = line[:d], line[d:]
        n, elts = line
        assert len(elts) == int(n)
        print 'Case #%d:' % (i + 1), solve(compounds, opposites, elts)

def solve(_compounds, _opposites, elts):
    compounds = {}
    for a, b, c in _compounds:
        compounds[a, b] = c
        compounds[b, a] = c
    opposites = {}
    for a, b in _opposites:
        opposites.setdefault(a, set()).add(b)
        opposites.setdefault(b, set()).add(a)
    outcome = []
    for elt in elts:
        if outcome and (outcome[-1], elt) in compounds:
            outcome[-1] = compounds[outcome[-1], elt]
        elif elt in opposites and any(x in outcome for x in opposites[elt]):
            del outcome[:]
        else:
            outcome.append(elt)
    return '[%s]' % ', '.join(outcome)

if __name__ == '__main__':
    sys.exit(main())
