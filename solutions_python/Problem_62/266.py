#!/usr/bin/python

from __future__ import division

import sys
import re

def rdln(regex):
    s = sys.stdin.readline()
    matcher = re.match(regex, s)
    if matcher is None:
        raise ValueError, "Can't match %s against %s" % (s, regex)
    return matcher.groups()

def main():
    (caseCount,) = map(int, rdln(r'(\d+)'))
    for case in range(caseCount):
        (wireCount,) = map(int, rdln(r'(\d+)'))
        wires = []
        for n in range(wireCount):
            a, b = map(int, rdln(r'(\d+) (\d+)'))
            wires.append((a, b))
            
        isects = list(intersections(wires))
        print "Case #%d: %d" % (case + 1, len(isects) // 2)

def intersections(wires):
    for wire1 in wires:
        a1, b1 = wire1
        for wire2 in wires:
            a2, b2 = wire2
            if b1 - a1 == b2 - a2:
                continue

            x = (a1 - a2) / ((a1 - a2) - (b1 - b2))

            if 0.0 <= x <= 1.0:
                yield (wire1, wire2)

if __name__ == '__main__':
    main()
