#!/usr/bin/python
import sys

T = int(sys.stdin.readline())
for test_case in xrange(1, T+1):
    A, N = map(int, sys.stdin.readline().split())
    motes = map(int, sys.stdin.readline().split())
    best = N
    if A > 1:
        motes.sort()
        size = A
        adds = 0
        for last in xrange(0, N): # last mote passed thru adding
            #print size, adds, motes
            while size <= motes[last]:
                size += size - 1
                adds += 1
            size += motes[last]
            best = min(best, adds+(N-last-1))
    print "Case #{0}: {1}".format(test_case, best)
        
