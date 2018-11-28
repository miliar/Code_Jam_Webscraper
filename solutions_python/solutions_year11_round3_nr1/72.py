#!/usr/bin/env python
# encoding: utf-8
"""
SquareTiles.py

Created by Graham Dennis on 2011-05-22.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.
"""

import sys

def solve(R, C, picture):
    for r in xrange(R):
        for c in xrange(C):
            if picture[r][c] != '#': continue
            if r == R-1 or c == C-1: return False
            if picture[r+1][c] != '#' or \
               picture[r][c+1] != '#' or \
               picture[r+1][c+1] != '#':
               return False
            
            picture[r][c] = picture[r+1][c+1] = '/'
            picture[r+1][c] = picture[r][c+1] = '\\'
    return True

def main():
    f = open(sys.argv[1])
    T = int(f.readline())
    
    for t in xrange(T):
        R, C = map(int, f.readline().split())
        picture = [list(f.readline().strip()) for _ in xrange(R)]
        
        possible = solve(R, C, picture)
        
        print "Case #%i:" % (t + 1)
        print '\n'.join(''.join(line) for line in picture) if possible else "Impossible"

if __name__ == "__main__":
    sys.exit(main())
