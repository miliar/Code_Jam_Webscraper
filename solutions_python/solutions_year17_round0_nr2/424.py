#!/usr/bin/env python

import sys

def solve(N):
    digits = [int(s) for s in N]
    i = 0
    for i in xrange(len(digits)-1):
        if digits[i] > digits[i+1]:
            # i now is the leftmost illegal digit (which is larger than its rightmost neighbour)
            k = i
            while (k > 0 and digits[k-1] == digits[i]):
                k -= 1
            digits[k] -= 1
            for j in xrange(k+1, len(digits)):
                digits[j] = 9
            break
    result = "".join(str(d) for d in digits)
    return int(result)
    
if __name__ == "__main__":
    inp = open(sys.argv[1], 'r').readlines()
    T = int(inp[0])
    for t in xrange(T):
        N = inp[t+1].strip()
        print "Case #%d: %d" % (t+1, solve(N))
