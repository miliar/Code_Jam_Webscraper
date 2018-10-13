#!/usr/bin/env python

"""Google Code Jam, Online Round 1."""

import sys
import math
import re
from mpmath import *

def useage():
    """Prints useage instructions."""
    print "useage: " + sys.argv[0] + " FILE"
    print "where FILE is the path and name of a valid input file"

def main(args):
    """Point of code entry.  Command name in args[0], any additional args
    passed are in the remainder of the args array."""
    if len(args) < 2:
        useage()
        return 1
    num_cases = -1
    mp.dps = 30
    base = mpf(3) + (mpf(5) ** 0.5)

    try:
        f = open(args[1])
        num_cases = int(f.readline())
        assert 0 < num_cases <= 100
        for case in xrange(num_cases):
            n = mpf(f.readline())
            assert (2 <= n <= 2000000000)
            ans = str(base**n)
            idx = ans.find('.')
            if idx > 2: ans = '%03d' % int(ans[idx -3:idx])
            else: ans = '%03d' % int(ans[:idx])
            print "Case #" + str(case+1) + ": " + ans
    except IOError:
        print "Invalid file input"
        useage()
        return 2

if __name__ == '__main__':
    sys.exit(main(sys.argv))
