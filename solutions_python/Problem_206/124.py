#!/bin/python3

T = int(input().strip())
for test in range(T):
    D, N = [int(x) for x in input().split()]
    comps = []
    for i in range(N):
        K, S = [float(x) for x in input().split()]
        comps.append((K, S))
    # srtcmp = sorted(comps, key=lambda x: ((D - x[0]) / x[1]))
    # lim = srtcmp[0]
    # print (lim)
    # ans = D / ((D - lim[0]) / lim[1])
    ans = min([((D * x[1]) / (D - x[0])) for x in comps])
    print('Case #%d: %f' % ((test + 1), ans))
