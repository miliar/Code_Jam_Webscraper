#!/usr/bin/env python
# encoding: utf-8
"""
Magicka.py

Created by Graham Dennis on 2011-05-07.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.
"""

import sys


def main():
    f = open(sys.argv[1])
    T = int(f.readline())
    
    for t in xrange(T):
        items = f.readline().split()
        C = int(items.pop(0))
        combiningElements = items[:C]
        del items[:C]
        D = int(items.pop(0))
        opposedElements = items[:D]
        del items[:D]
        N = int(items.pop(0))
        invoked = items[0]
        assert len(items) == 1
        
        combiningDict = dict([(frozenset(c[:2]), c[2]) for c in combiningElements])
        opposedDict = dict()
        for a, b in opposedElements:
            opposedDict.setdefault(a, set()).add(b)
            opposedDict.setdefault(b, set()).add(a)
        
        elementList = []
        for element in invoked:
            
            if elementList and frozenset((element, elementList[-1])) in combiningDict:
                elementList[-1] = combiningDict[frozenset((element, elementList[-1]))]
            elif opposedDict.get(element, set()).intersection(elementList):
                del elementList[:]
            else:
                elementList.append(element)
        
        
        print "Case #%i: [%s]" % (t+1, ', '.join(elementList))

if __name__ == "__main__":
    sys.exit(main())
