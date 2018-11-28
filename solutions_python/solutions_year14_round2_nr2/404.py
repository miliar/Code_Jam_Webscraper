import sys

sys.stdin = open("B-small-attempt0.in", "r")

def solve():
    a,b,k = map(int, sys.stdin.readline().strip().split())
    res = 0
    for i in xrange(a):
        for j in xrange(b):
            if (i & j) < k:
                res += 1
    return res
T = int(input())
for _t in xrange(T): 
    print "Case #" +str(_t+1) + ": " + str(solve())