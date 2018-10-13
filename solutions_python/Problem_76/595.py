#!/usr/bin/python

import sys
import operator

#import psyco
#psyco.full()

def main():
    # Read in
    infile = open(sys.argv[1])
    numtests = int(infile.readline())
    for i in range(numtests):
        numcandies = int(infile.readline())
        candies = [int(x) for x in infile.readline().split()]
        candies.sort()
    
        if candies[0] == reduce(operator.xor, candies[1:]):
            result = sum(candies[1:])
        else:
            result = "NO"
        print "Case #%d: %s" % (i+1, result)

if __name__ == "__main__":
    main()
