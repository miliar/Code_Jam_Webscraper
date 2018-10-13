#!/usr/bin/env python

from sys import stdin, stderr
from math import ceil, floor

T = int(stdin.readline())

def clean(data, thre):
    for d in data:
        while len(d) > 0 and d[0] < thre: del d[0]
        pass
    return

def Solve(need, data):
    ret = 0
    for n, d in zip(need, data):
        for i in range(len(d)):
            d[i] = float(d[i]) / n
            pass
        pass
    while True:
        for d in data:
            if len(d) == 0: return ret
            pass
        head = [d[0] for d in data]
        next_raw_amount = min(head)
        next_min = int(ceil(next_raw_amount  / 1.1))
        next_max = int(floor(next_raw_amount / 0.9))
        if next_min > next_max:
            clean(data, next_min * 0.9)
            continue
            pass
        is_ok = True
        for h in head:
            if h > next_max * 1.1:
                is_ok = False
                break
            pass
        if is_ok:
            ret += 1
            for d in data: del d[0]
            pass
        else:
            clean(data, (next_max+1) * 0.9)
            pass
        pass
    return ret

# for i in range(100):
#     print Solve('A' * 1000)
# exit(0)


for t in range(T):
    N, P = tuple([int(v) for v in stdin.readline().split()])
    need = [int(v) for v in stdin.readline().split()]
    data = []
    for i in range(N):
        data.append([int(v) for v in stdin.readline().split()])
        data[-1].sort()
        pass

    print "Case #%d:" % (t+1),
    #print N,
    print Solve(need, data)
