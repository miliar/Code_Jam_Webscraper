#!/usr/bin/env python

import numpy as np

infile = file("in.txt", "r")
outfile = file("out.txt", "w")

T = int(infile.readline())
for i in range(1, T+1):
    # input
    data = infile.readline().replace("\n", "").split(" ")
    N = int(data[0])
    S = int(data[1])
    p = int(data[2])
    totals = [int(j) for j in data[3:]]
    # no surprise
    optimal = np.zeros(N)
    for j in range(N):
        tmp = totals[j]
        if (tmp%3 == 0):
            optimal[j] = tmp/3
        elif (tmp%3 == 1):
            optimal[j] = (tmp+2)/3
        else:
            optimal[j] = (tmp+1)/3
    # first sweep, find the first loser
    rank = optimal.argsort()
    rank = rank[::-1]
    for cut in range(N):
        if optimal[rank[cut]] < p:
            break
    result = cut
    # stupid python, cut = N-1
    if (cut == N-1) and (optimal[rank[cut]] >= p):
        result = result + 1
        cut = cut + 1        
    # greedy surprise allocation, save the loser?
    while (S > 0) and (cut < N):
        tmp = totals[rank[cut]]
        # big loser, no hope
        if ((tmp+4)/3) < p:
            break
        # saveable?
        if (tmp>0) and (tmp%3 == 0) and (tmp/3+1 >= p):
            result = result + 1
            S = S - 1
        elif (tmp%3 == 2) and ((tmp+4)/3 >=p):
            result = result + 1
            S = S - 1
        cut = cut + 1
    # output
    outfile.write("Case #{}: {}\n".format(i, result))

outfile.close()


