#!/usr/bin/python
import sys
# First, get the input as a bidimensional list, N x M.

def is_possible(A,N,M):
    # Loop through every entry.
    rowmax = [ max(A[n]) for n in xrange(N) ]
    colmax = [ max(A[i][m] for i in xrange(N)) for m in xrange(M) ]
    # rowmax[n]: max of row n.
    # colmax[m]: max of col m.
    for n in xrange(N):
        for m in xrange(M):
            # A[n][m] must be the max of its row or column.
            current = A[n][m]
            if current != rowmax[n] and current != colmax[m]:
                return "NO"
    return "YES"

T = int(raw_input())
for t in xrange(T):
    N,M = map(int,raw_input().split(" "))
    A = [ [int(n) for n in raw_input().split(" ")] for _ in xrange(N)]
    # Process A
    print "Case #" + str(t+1) + ":", is_possible(A,N,M)


        

    
