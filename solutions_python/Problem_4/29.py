#!/usr/bin/env python

"""Google Code Jam, Online Round 1."""

import sys

def useage():
    """Prints useage instructions."""
    print "useage: " + sys.argv[0] + " FILE"
    print "where FILE is the path and name of a valid input file"

def read_from(fh, num):
    """Reads num lines from the open filehandle fh.  Returns lines as a list.
    Assumes fh is open and contains at least num lines from current offset"""
    return [fh.readline() for i in xrange(num)]

def main(args):
    """Point of code entry.  Command name in args[0], any additional args
    passed are in the remainder of the args array."""
    if len(args) < 2:
        useage()
        return 1
    num_cases = -1
    try:
        f = open(args[1])
        num_cases = int(f.readline())
        for case in xrange(num_cases):
            vec_len = int(f.readline())
            v1 = [int(i) for i in f.readline().split()]
            v2 = [int(i) for i in f.readline().split()]
            v1.sort()
            v2.sort()
            tot = 0
            for i in xrange(vec_len):
                tot += v1[i] * v2[-(i+1)]
            print "Case #" + str(case+1) + ": " + str(tot)
    except IOError:
        print "Invalid file input"
        useage()
        return 2

if __name__ == '__main__':
    sys.exit(main(sys.argv))
