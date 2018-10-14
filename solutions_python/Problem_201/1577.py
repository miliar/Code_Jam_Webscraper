#!/usr/bin/env python

import sys
import heapq

#@profile
def solve(*args):
    (N, K) = args
    
    # trivia
    if N == K:
        return "0 0"
    
    B = [-N]
    heapq.heapify(B)
    for k in xrange(K):
        n = -heapq.heappop(B)
        Ls = n/2
        Rs = n - Ls - 1
        if Ls > 0:
            heapq.heappush(B, -Ls)
            heapq.heappush(B, -Rs)
        #print [Ls, Rs], B
    
    return "{} {}".format(Ls, Rs)

def main():
    T = int(sys.stdin.readline())
    for caseNumber in xrange(1, T+1):
        params = [int(one.strip()) for one in sys.stdin.readline().split(" ")]
        result = solve(*params)
        print "Case #%d: %s" % (caseNumber, result)
        #break
        
if __name__ == '__main__':
    main()


