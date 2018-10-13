#!/usr/bin/env python

import sys
import operator

# R
# Y
# B
# O = R Y
# G = Y B
# V = R B


def solve(*args):
    (N, R, O, Y, G, B, V) = args
    
    if Y > R + B or R > Y + B or B > Y + R:
        return "IMPOSSIBLE"

    U = {
        "R":R,
        "Y":Y,
        "B":B
    }
    
    ret = ""
    for n in xrange(N):
        if n == N-2:
            if len(U) == 2:
                if U.keys()[0] == ret[0]:
                    if U.keys()[0] == ret[-1]:
                        return "IMPOSSIBLE"
                    else:
                        return ret + U.keys()[0] + U.keys()[1]
                if U.keys()[1] == ret[0]:
                    if U.keys()[1] == ret[-1]:
                        return "IMPOSSIBLE"
                    else:
                        return ret + U.keys()[1] + U.keys()[0]
        S = sorted(U.items(), key=operator.itemgetter(1), reverse=True)
        for s in S:
            if ret[-1:] == s[0]:
                continue

            ret += s[0]
            if s[1] == 1:
                U.pop(s[0])
            else:
                U[s[0]] -= 1
            break
        
    return ret

def main():
    T = int(sys.stdin.readline())
    for caseNumber in xrange(1, T+1):
        result = solve(*map(int, sys.stdin.readline().split()))
        print "Case #%d: %s" % (caseNumber, result)
       
if __name__ == '__main__':
    main()


