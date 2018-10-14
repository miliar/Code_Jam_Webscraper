#!/usr/bin/env python
# encoding: utf-8
"""
PerfectHarmony.py

Created by Graham Dennis on 2011-05-22.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.
"""

import sys


def main():
    f = open(sys.argv[1])
    T = int(f.readline())
    
    for case in xrange(T):
        N, L, H = map(int, f.readline().split())
        frequencies = map(int, f.readline().split())
        
        reallyPossible = False
        for p in xrange(L, H+1):
            possible = True
            for freq in frequencies:
                if max(p, freq) % min(p, freq) != 0:
                    possible = False
                    break
            if possible:
                reallyPossible = True
                break
        
        result = str(p) if reallyPossible else "NO"
        print "Case #%i: %s" % (case + 1, result)

if __name__ == "__main__":
    sys.exit(main())
