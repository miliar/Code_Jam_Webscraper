from sys import stdin as fp
import math

def solve(A, B, K):
    wins = 0
    for i in range(A):
        for j in range(B):
            if i & j < K:
                wins += 1
    return wins

def dig(x):
    return int(math.floor(math.log(x, 2))) + 1

T = int(fp.readline())
for i in xrange(T):
    A, B, K = map(int, fp.readline().split())
    print "Case #%s: %s" % (i+1, solve(A, B, K))    
