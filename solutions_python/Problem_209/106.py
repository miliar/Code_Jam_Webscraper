# Google Codejam 2017: Round 1C
# Problem A: Ample Syrup
# Author: Mahmoud Aladdin <aladdin3>

import sys
from math import pi

sys.setrecursionlimit(3000)

dp = {}
pancakes = []

def solveDP(n, k):
    #print dp, pancakes
    if k == 0: return 0
    if n >= len(pancakes): return -10000000

    if (n, k) not in dp:
        hV = 2 * pi * pancakes[n][0] * pancakes[n][1]
        uV = pi * (pancakes[n][0] ** 2) 

        takeIt = solveDP(n + 1, k - 1)
        takeIt += hV 
        if k == 1:
            takeIt += uV

        leaveIt = solveDP(n + 1, k)
        dp[(n, k)] = max(takeIt, leaveIt)
    return dp[(n, k)]

def solve(cn):
   # print "HERE"
    n, k = map(int, raw_input().strip().split())

    global dp
    global pancakes
    dp = {}
    pancakes = []

    for i in xrange(n):
        ki, si = map(int, raw_input().strip().split())
        pancakes.append((ki, si))
        
    pancakes.sort()
    #print pancakes
    result = solveDP(0, k)

    print "Case #{0}: {1:0.8f}".format(cn, result)
    print >> sys.stderr, "Case #{0}: {1:0.8f}".format(cn, result)
    

if __name__ == "__main__":
    cn = input()
    for i in xrange(cn):
        solve(i + 1)