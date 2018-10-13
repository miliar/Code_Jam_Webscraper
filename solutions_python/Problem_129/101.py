#! /usr/bin/env python

from bisect import bisect_left

MOD = 1000002013

class OP:
    def __init__(self, o, p):
        self.o = o
        self.p = p

class EP:
    def __init__(self, e, p):
        self.e = e
        self.p = p

def get_cost(e, o):
    return int((e - o) * (e - o - 1) / 2)

T = int(input())
for TT in range(1, T + 1):
    ocost = 0
    cost = 0
    ans = 0
    n, m = [int(x) for x in input().split()]
    ops = []
    eps = []
    for i in range(m):
        o, e, p = [int(x) for x in input().split()]
        ops.append(OP(o, p))
        eps.append(EP(e, p))
        # ops[i].o, ops[i].p = o, p
        # eps[i].e, eps[i].p = e, p
        ocost -= p * get_cost(e, o)
    ops.sort(key = lambda op: op.o)
    eps.sort(key = lambda ep: ep.e)
    ops.reverse()

    keys = [eps[i].e for i in range(m)]
    keyp = [eps[i].p for i in range(m)]

    for i in range(m):
        j = bisect_left(keys, ops[i].o)
        while ops[i].p > 0:
            if ops[i].p >= eps[j].p:
                cost -= eps[j].p * get_cost(eps[j].e, ops[i].o)
                ops[i].p -= eps[j].p
                eps[j].p = 0
                j += 1
            else:
                cost -= ops[i].p * get_cost(eps[j].e, ops[i].o)
                eps[j].p -= ops[i].p
                ops[i].p = 0

    ans = (ocost - cost) % MOD
    print("Case #" + str(TT) + ": " + str(ans))
