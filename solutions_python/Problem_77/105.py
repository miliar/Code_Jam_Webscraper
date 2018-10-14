#!/usr/bin/env python
# encoding: utf-8
"""
GoroSort.py

Created by Graham Dennis on 2011-05-07.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.
"""

import sys

def main():
    f = open(sys.argv[1])
    T = int(f.readline())
    x = [0.0] * 1005
    
    for i in xrange(2, 1005):
        leadingProbability = 1.0
        x[i] = 0.0
        for j in xrange(1, i):
            x[i] += leadingProbability / (i - j + 1) * (x[j] + x[i-j] + (1 if j > 1 else 0))
            leadingProbability *= (1 - 1.0/(i-j+1))
        x[i] += leadingProbability
        x[i] /= (1.0 - leadingProbability)
    
    x[1] = -1
    
    for t in xrange(T):
        N = int(f.readline())
        numbers = map(int, f.readline().split())
        remainingToVisit = set(numbers)
        cycleLengths = []
        while remainingToVisit:
            element = remainingToVisit.pop()
            cycle = set((element,))
            while numbers[element-1] not in cycle:
                cycle.add(numbers[element-1])
                remainingToVisit.remove(numbers[element-1])
                element = numbers[element-1]
            cycleLengths.append(len(cycle))
        
        
        print "Case #%i: %f" % (t+1, sum(1 + x[i] for i in cycleLengths))

if __name__ == "__main__":
    sys.exit(main())
