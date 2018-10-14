import numpy as np
import itertools
t = int(raw_input())
for i in xrange(1, t + 1):
    n, k = [int(s) for s in raw_input().split(" ")]
    u = float(raw_input())
    arr = [float(s) for s in raw_input().split(" ")]
    # print arr
    arr = sorted(arr, key=float)
    maxr = 0.0
    for j in xrange(1, n + 1):
        sumk = sum(arr[:j])
        newavg = (sumk + u) / j
        if newavg < arr[j - 1]:
            break
        if newavg > 1.0:
            newavg = 1.0
        news = 1.0
        for l in xrange(n-1, -1, -1):
            if l < j:
                news *= newavg
            else:
                news *= arr[l]
        if news > maxr:
            maxr = news

    print "Case #{}: {}".format(i, maxr)
