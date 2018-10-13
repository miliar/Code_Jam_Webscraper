#! /usr/bin/python2.7

def solve(s, k):
    length = len(s)
    mask = 2 ** k - 1
    num = int("".join(map(str, s)), 2)
    rv = 0
    for i in xrange(length - k + 1):
        if num % 2 == 0:
            rv += 1
            num ^= mask
        num /= 2
    if num != mask / 2:
        return "IMPOSSIBLE"
    return rv
        
import sys
f = sys.stdin
#f = open("q1_example.in")
T = int(f.readline())
for i in xrange(1, T + 1):
    S, K = f.readline().split()
    K = int(K)
    S = map(lambda x: {"-": 0, "+": 1}[x], S)
    print "Case #%d: %s" % (i, solve(S, K))