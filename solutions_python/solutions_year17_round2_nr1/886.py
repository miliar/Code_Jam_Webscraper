# /usr/bin/env python
# -*- coding: utf8 -*-
import numpy as np

if __name__ == '__main__':
    T = int(input())
    for ti in range(T):
        D, N = [int(e) for e in input().split()]
        K, S = np.zeros(N), np.zeros(N)
        for i, Hi in enumerate(range(N)):
            K[i], S[i] = [float(e) for e in input().split()]
        arrival = (D - K) / S
        tmax = np.max(arrival)
        velocity = D / tmax
        print("Case #{}: {}".format(ti + 1, velocity))
