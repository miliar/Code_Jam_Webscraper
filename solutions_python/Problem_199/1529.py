#!/usr/bin/env python

import time
import sys

#@profile
def flip(s):
    return s.replace("+", ".").replace("-", "+").replace(".", "-")
    
#@profile
def solve(*args):
    (S, K) = args
    K = int(K)

    # trivial cases
    if "-" not in S:
        return 0
        
    retval = 0
    s = S
    while "-" in s:
        f = s.find("-")
        if K + f > len(S):
            return "IMPOSSIBLE"
        s = s[0:f] + flip(s[f:f+K]) + s[f+K:]
        retval += 1

    return retval
    

def main():
    T = int(sys.stdin.readline())
    for caseNumber in xrange(1, T+1):
        result = solve(*sys.stdin.readline().strip().split())
        print "Case #%d: %s" % (caseNumber, result)
       
    # for caseNumber in range(10000):
    #     result = solve(caseNumber)
    #     print "Case #%d: %s" % (caseNumber, result)

if __name__ == '__main__':
    main()


