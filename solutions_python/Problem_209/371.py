#!/usr/bin/env python
from itertools import combinations
import math

def case(T):
    N, K = map(int, input().split())
    pancakes = [list(map(int, input().split())) for i in range(N)]
    panlist = combinations(pancakes, K)
    #return max([area(sorted(p)) for p in panlist])
    m = 0
    for p in panlist:

        sortedp = sorted(p)
        m = max(m, area(sortedp))
        #print(sortedp, area(sortedp))

    return m

def area(plist):
    c = 0
    R_prev = 0
    for R, H in plist:
        c += math.pi * (R**2 - R_prev**2)
        c += 2 * math.pi * R * H
        R_prev = R
    return c



if __name__=="__main__":
    for i in range(int(input())):
        print("Case #{}: {}".format(i+1, case(i)))
