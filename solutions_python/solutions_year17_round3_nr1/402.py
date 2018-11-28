import sys
import numpy as np
from math import *
from copy import deepcopy
from itertools import product, permutations, combinations
from Queue import Queue


sys.setrecursionlimit(3000)

def lat_area(pa):
    r, h = pa
    return pi * r**2

def sub_area(pa):
    r, h = pa

    return 2 * pi * r * h

def P(d):
    for x in d:
        print x

for test in range(1, int(raw_input()) + 1):
    n, k = map(int, raw_input().split())
    data = [map(int, raw_input().split()) for _ in range(n)]

    data.sort(reverse=True)

    #print lat_area(data[1]) + sub_area(data[1]) + 0#lat_area(data[1])
    #print lat_area(data[1]) + sub_area(data[1]) + sub_area(data[2])#lat_area(data[1])
    #print lat_area(data[1]) + sub_area(data[1]) + lat_area(data[2])

    #print data

    dp = [[0 for _ in range(n + 1)] for _ in range(k + 1)]
    #P(dp)
    answer = 0
    for i in range(1, k + 1):
        for j in range(1, n + 1):
            v = dp[i - 1][j - 1] + sub_area(data[j - 1])
            if i == 1:
                v += lat_area(data[j - 1])

            dp[i][j] = max(dp[i][j - 1], v)

            answer = max(answer, dp[i][j])

    #print "---"
    #P(dp)

    print 'Case #{}: {:.9f}'.format(test, answer)

