#!/usr/bin/env python
# encoding: utf-8
"""
B.py

Created by Graham Dennis on 2012-04-14.
Copyright (c) 2012 __MyCompanyName__. All rights reserved.
"""

import sys

def main():
    f = open(sys.argv[1])
    T = int(f.readline())
    
    for t in xrange(T):
        scores = map(int, f.readline().split())
        N = scores.pop(0)
        S = scores.pop(0)
        p = scores.pop(0)
        scores.sort()
        numBetterThanP = 0
        for score in reversed(scores):
            if score/3 >= p:
                numBetterThanP += 1
            elif score/3 == p-1 and (score % 3) == 0:
                if S > 0 and 0< score/3 < 10:
                    numBetterThanP += 1
                    S -= 1
            elif score/3 == p-1 and (score % 3) >= 1:
                numBetterThanP += 1
            elif score/3 == p-2 and (score % 3) == 2:
                if S > 0:
                    numBetterThanP += 1
                    S -= 1
        
        print "Case #%i: %i" % (t+1, numBetterThanP)

if __name__ == "__main__":
    sys.exit(main())
