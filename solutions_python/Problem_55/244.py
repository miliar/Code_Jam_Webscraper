#!/usr/bin/env python
import sys
import operator

T = int(sys.stdin.readline())

for tt in xrange(T):
    R,K,N = [int(x) for x in sys.stdin.readline().split()]
    line = [int(x) for x in sys.stdin.readline().split()]
    turn = 0
    res = 0
    i = 0
    s = 0
    if sum(line) <= K:
        res = R * sum(line)
    else:
        while 1:
            s += line[i]
            if s > K: 
                res += s - line[i]
                turn += 1
                s = 0
                if turn == R: 
                    break
            else:
                i = (i + 1) % N


    print "Case #%d: %d" % (tt+1, res)
