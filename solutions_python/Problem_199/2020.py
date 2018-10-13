#!/bin/env python2
import sys

def solve(S, K):
    K -= 1  # not include the right most one
    flip = 0
    while S:
        right = S.pop()
        if not right:
            if len(S) < K:
                return "IMPOSSIBLE"
            S[-K:] = [ not i for i in S[-K:] ]
            flip += 1
    return flip

def main():
    f = open( sys.argv[1] )
    #f = sys.stdin
    T = int( f.next().strip() )
    for n, line in enumerate(f):
        S, K = line.strip().split()
        S = [ i == "+" for i in S ]
        K = int(K)
        print "Case #{0}: {1}".format( n+1, solve(S, K) )

main()
