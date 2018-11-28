#!/usr/bin/env python
"outrage"

import sys

def outrage():
    N = int(sys.stdin.readline())
    for n in xrange(N):
        P, K, L = map(int, sys.stdin.readline().strip().split())
        freq = map(int, sys.stdin.readline().strip().split())
        freq.sort(reverse=True)
        #print P, K, L, freq
        if L > P*K:
            print "Case #%d: Impossible" % (n+1)
        else:
            sol = 0
            for i in range(len(freq)):
                col = (i / K) + 1
                sol += col * freq[i]
                #print col, freq[i], col * freq[i]
            print "Case #%d: %d" % (n+1, sol)
if __name__ == "__main__":
    outrage()
