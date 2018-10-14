#!/usr/bin/env python

import sys
import itertools

def solve():
    A, B, K = tuple(int(one) for one in sys.stdin.readline().split())
    
    retval = 0
    for a,b in itertools.product(range(A), range(B)):
        retval += int(a&b < K)
    return retval
#enddef

def main():
    T = int(sys.stdin.readline())
    for caseNumber in xrange(1, T+1):
        print "Case #%d: %s" % (caseNumber, solve())
    #endfor
#enddef

if __name__ == '__main__':
    main()
#endif


