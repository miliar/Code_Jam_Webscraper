#!/usr/bin/env python2.7
# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
import math
def getMaxMin(N, K):
    h = int(math.floor(math.log(K, 2)))
    pow_h = pow(2,h)
    pos_of_nodes_in_h = K - (pow_h - 1)
    max_v_in_h = int(math.floor(N/pow_h))
    x = N - (pow_h * max_v_in_h) + 1
    max_space = max_v_in_h
    if pos_of_nodes_in_h > x:
        max_space = max_v_in_h - 1
    if max_space % 2 == 0:
        return int(max_space/2), int(max_space/2) -1
    else:
        return int((max_space-1)/2), int((max_space-1)/2)

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    N, K = [int(s) for s in raw_input().split(' ')]
    maxV, minV = getMaxMin(N, K)
    print "Case #{}: {} {}".format(i, maxV, minV)
