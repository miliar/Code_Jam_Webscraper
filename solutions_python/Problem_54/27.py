#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Graham Dennis on 2010-05-08.
Copyright (c) 2010 __MyCompanyName__. All rights reserved.
"""

import sys

def greatestCommonFactor(a, b):
    if a < b:
        a, b = b, a
    if b == 0: return a
    return greatestCommonFactor(b, a - b * (a // b))


def main(argv=None):
    if argv is None:
        argv = sys.argv
    f = file(sys.argv[1])
    
    C = int(f.readline())
    for c in xrange(C):
        stuff = map(int, f.readline().split())
        N, events = stuff[0], list(set(stuff[1:]))
        events.sort()
        differences = [a - b for a, b in zip(events[1:], events[:-1])]
        gcf = differences[0]
        for b in differences[1:]:
          gcf = greatestCommonFactor(gcf, b)
        print 'Case #%i: %s' % (c+1, -events[0] % gcf)
        
        # print 'Case #%i: %s' % (c+1, result)
    


if __name__ == "__main__":
    sys.exit(main())
