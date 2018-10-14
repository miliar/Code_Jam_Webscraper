#!/usr/bin/python2
# -*- coding: utf-8 -*-
# †
from collections import defaultdict

def f(N, K):
    if K == 1:
        maxi = N / 2
        mini = (N - 1) / 2
        return maxi, mini
    dic = defaultdict(int)
    a = N - 1
    dic[a] = 1

    ndic = defaultdict(int)
    for k, v in dic.items():
        smaller = (k - 2) / 2
        larger  = (k - 1) / 2
        ndic[smaller] += v
        ndic[larger]  += v
    dic = ndic

    loop = 1
    while True:
        keys = list(dic.keys())
        keys.sort(reverse=True)
        if 2 ** loop <= K < 2 ** (loop + 1):
            start = 2 ** loop
            cur   = 2 ** loop
            for k in keys:
                cur += dic[k]
                if K < cur:
                    return (k+1) / 2, k / 2
            raise
        ndic = defaultdict(int)
        for k, v in dic.items():
            smaller = (k - 2) / 2
            larger  = (k - 1) / 2
            ndic[smaller] += v
            ndic[larger]  += v
        dic = ndic
        loop += 1



T = int(raw_input())
for case in xrange(T):
    N, K = map(int, raw_input().split())
    maxi, mini = f(N, K)
    print 'Case #{}: {} {}'.format(case+1, maxi, mini)
