#!/bin/python3

# import math
from collections import Counter

T = int(input().strip())
for test in range(T):
    N, P = [int(x) for x in input().split()]
    divisors = [int(x) for x in input().split()]
    # quants = {}
    norms = {}
    # maxnorm = 0
    # minnorm = math.inf
    for i in range(N):
        vals = [(int(x) / divisors[i]) for x in input().split()]
        vals.sort()
        # upvals = [round(x) for x in vals if ((round(x) > 0) and
        #                                      ((abs(x - round(x) / round(x))) <= 0.1))]
        # print ( vals,upvals)
        # if (math.floor(vals[0]) < minnorm):
        #     minnorm = math.floor(vals[0])
        # if (math.ceil(vals[-1]) > maxnorm):
        #     maxnorm = math.ceil(vals[-1])
        norms[i] = vals
        # norms[i] = Counter(upvals)

    # print(norms)
    ans = 0
    # for val in norms[0]:
    #     ans += norms[min(norms, key=lambda x:norms[x].get(val, 0))].get(val, 0)
    pointers = [0] * N
    while P not in pointers:
        minpoint = 0
        mining = 0
        s = 0
        for i in range(N):
            if norms[i][pointers[i]] < norms[mining][pointers[minpoint]]:
                minpoint = pointers[i]
                mining = i
            s += norms[i][pointers[i]]
        avg = s / N
        cnt = round(avg)
        goodpack = True
        for i in range(N):
            val = norms[i][pointers[i]]
            if ((cnt > 0) and (abs(val - cnt) <= (0.100000001 * cnt))):
                goodpack = goodpack
            else:
                # print(pointers)
                # print(abs(val-cnt),cnt)
                goodpack = False
                break
        if goodpack:
            ans += 1
            for i in range(N):
                pointers[i] += 1
        else:
            pointers[mining] += 1

    print('Case #%d: %d' % ((test + 1), ans))
