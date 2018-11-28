#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Graham Dennis on 2010-05-23.
Copyright (c) 2010 __MyCompanyName__. All rights reserved.
"""

import sys


def main():
    f = file(sys.argv[1])
    
    T = int(f.readline())
    for t in xrange(T):
        N = int(f.readline())
        AB = [tuple(map(int, f.readline().split())) for _ in xrange(N)]
        
        result = 0
        for idx, (a, b) in enumerate(AB):
            for a_, b_ in AB[idx+1:]:
                if b - b_ + a_ - a == 0: continue
                x = float(a_-a)/(b-b_ + a_-a)
                if 0 < x < 1:
                    # print (a, b), (a_, b_), x
                    result += 1
                
        print "Case #%i: %i" % (t+1, result)
    
    


if __name__ == '__main__':
    main()

