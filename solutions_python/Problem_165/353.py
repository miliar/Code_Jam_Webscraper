from math import sqrt, pow, log, ceil, log10, floor
from sys import stdin, setrecursionlimit
import copy
import random

setrecursionlimit(100000)
debug = 0

# Goal: find the minimal time such that we're certain to have the boat
def solve(R, C, W):

    # For R = 1
    # return int(ceil(C*1./W) + (W-1))

    # For R
    X = R * floor(C*1./W)
    if C % W != 0:
        X += 1

    X += (W-1)
    return int(X)


T = int(stdin.readline())

for i in range(1,T+1):
    
    R, C, W = map(int, stdin.readline().split(' '))
    
    print "Case #" + str(i) + ":", 

    if debug:
        print
        print R, C, W

    rep = solve(R, C, W)

    print rep
