#!/usr/bin/env python

import sys
# import numpy
import operator

def main(filename):
    
    f = open(filename, 'r')
    T = int(f.readline())
    
    for t in xrange(T):
        result = solve(f)
        
        print "Case #%i: %s" % (t+1, result)


def solve(f):
    first_row = int(f.readline())
    first_arrangement = [map(int, f.readline().split()) for _ in xrange(4)]
    
    first_possibilities = set(first_arrangement[first_row-1])
    
    second_row = int(f.readline())
    second_arrangement = [map(int, f.readline().split()) for _ in xrange(4)]
    
    second_possibilities = set(second_arrangement[second_row - 1])
    
    possibilities = first_possibilities.intersection(second_possibilities)
    
    if len(possibilities) == 0:
        return "Volunteer cheated!"
    elif len(possibilities) == 1:
        return list(possibilities)[0]
    else:
        return "Bad magician!"


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))