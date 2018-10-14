#!/usr/bin/env python

import time
import sys
    
def solve(*args):
    (N,) = args
    
    for i in xrange(len(N)-2, -1, -1):
        if N[i+1] < N[i]:
            if N[i] > 0:
                N[i] -= 1
                for j in xrange(len(N)-1, i, -1):
                    N[j] = 9
    
    return int("".join(map(str,N)))


def main():
    T = int(sys.stdin.readline())
    for caseNumber in xrange(1, T+1):
       result = solve([int(one) for one in sys.stdin.readline().strip()])
       print "Case #%d: %s" % (caseNumber, result)
       
    # for caseNumber in range(10000):
    #     result = solve(caseNumber)
    #     print "Case #%d: %s" % (caseNumber, result)

if __name__ == '__main__':
    main()


