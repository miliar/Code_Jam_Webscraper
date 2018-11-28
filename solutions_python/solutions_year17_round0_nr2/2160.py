#!/bin/env python2
import sys

def solve(N):
    i, j = len(N) - 1, 0
    while j < i:
        if N[j] > N[j+1]:
            break
        j += 1
    if i == j:
        return N
    tail = "9" * (i - j)
    head = N[:j+1]
    head = int(head) - 1
    head = solve( str(head) ) if head else ""
    return head + tail

def main():
    f = open( sys.argv[1] )
    #f = sys.stdin
    T = int( f.next().strip() )
    for n, line in enumerate(f):
        N = line.strip()
        print "Case #{0}: {1}".format( n+1, solve(N) )

main()
