#!/usr/bin/env python
# -*- coding:utf-8 -*-

import numpy as np


T = int(input())

for t in range(1, T + 1):
    D, N = map(int, input().split())
    K = []
    S = []
    for _ in range(N):
        k, s = map(int, input().split())
        K.append(k)
        S.append(s)
    if N == 1:
        ans = D / (abs(D - K[0]) / S[0])
    else:
        indices = np.argsort(K)[::-1]
        k = K[indices[0]]
        s = S[indices[0]]
        for i in range(N-1):
            after = indices[i]
            before = indices[i+1]
            if S[after] >= S[before]:
                k = K[before]
                s = S[before]
                continue
            hh = (D - K[after]) / S[after]
            h = (K[after] - K[before]) / (S[before] - S[after])
            if hh < h:
                k = K[before]
                s = S[before]
            else:
                k = K[after]
                s = S[after]
        h = (D - k) / s
        ans = D / h
    print("Case #{}: {:0.6f}".format(t, ans))
