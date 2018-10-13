#!/usr/bin/env python

import sys


def num_stream():
    for s in sys.stdin:
        for x in s.rstrip().split():
            yield int(x)

def solve(a1, order1, a2, order2):
    p = (a1 - 1) * 4
    cards = set(order1[p:p+4])
    p = (a2 - 1) * 4
    cards.intersection_update(set(order2[p:p+4]))
    if not cards:
        return "Volunteer cheated!"
    elif len(cards) == 1:
        return cards.pop()
    else:
        return "Bad magician!"

inp = num_stream()

T = next(inp)
for case in xrange(T):
    a1 = next(inp)
    order1 = [next(inp) for _ in xrange(16)]
    a2 = next(inp)
    order2 = [next(inp) for _ in xrange(16)]
    print "Case #%d: %s" % (case + 1, solve(a1, order1, a2, order2))

