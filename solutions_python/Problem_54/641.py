#!/usr/bin/env python
# encoding: utf-8
"""
fair-warning.py - Google Code Jam 2010

Copyright (c) 2010 David Jacot. All rights reserved.
"""

import sys

def gcd(a,b):        
    while a:
        a, b = b%a, a
    return b

if __name__ == '__main__':
    if len(sys.argv) != 2:
	    print "usage: fair-warning.py <filename>"
	    sys.exit()
	    
    with open(sys.argv[1]) as f:
        c = int(f.readline())
        i = 1
        for line in f:
            args = line.split()
            n = int(args[0])
            args = [int(a) for a in args[1:]]
            args.sort()
            
            a = args[0]
            b = args[1:]
            
            if n > 2:
                b = reduce(gcd, [x-a for x in b])
            else:
                b = b[0] - a
            
            t = b - a
            
            while t < 0:
                t += b
                
            print "Case #%d: %d" % (i, t)
            
            i += 1