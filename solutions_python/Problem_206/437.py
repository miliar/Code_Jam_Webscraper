#!/usr/bin/env python

import sys

def solve(*args):
    (D, N, horses) = args
    
    #print D, N, horses
    
    min_speed = max(h[1] for h in horses)
    max_distance = 0
    
    max_duration = 0
    for h in horses:
        max_duration = max(max_duration, (float(D) - h[0]) / h[1])
    
    return "%f" % (D / max_duration)
        
    return 0

def main():
    T = int(sys.stdin.readline())
    for caseNumber in xrange(1, T+1):
        D, N = map(int, sys.stdin.readline().split())
        horses = tuple(map(int, sys.stdin.readline().split()) for _ in xrange(N))
        result = solve(D, N, horses)
        print "Case #%d: %s" % (caseNumber, result)
        #print
        #print
       
if __name__ == '__main__':
    main()


