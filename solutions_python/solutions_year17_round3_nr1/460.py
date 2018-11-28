#!/usr/bin/env python3

import numpy as np
import random
import math
import itertools


def main():
    T = int(input())
    for t in range(1, T + 1):
        N, K = list(map(int, input().split()))
        RHA = []
        for i in range(N):
            R, H = list(map(int, input().split()))
            A = 2 * math.pi * R * H
            RHA.append((R, H, A))

        maxa = 0
        for b in range(N):
            first = RHA[b]
            RHA_s = [x for x in RHA if x[0] <= RHA[b][0]]
            RHA_s.remove(first)
            RHA_s = sorted(RHA_s, key=lambda x: x[2], reverse=True)
            # print(b)
            # print(RHA[b:b+K])
            # print(math.pi * RHA[b][0]**2)
            # print(sum([x[2] for x in RHA][b:b+K]))
            # print(math.pi * RHA[b][0]**2 + sum([x[2] for x in RHA][b:b+K]))
            maxa = max(math.pi * first[0]**2 + first[2] + sum([x[2] for x in RHA_s][0:K-1]), maxa)

        print("Case #" + str(t) + ": " + str(maxa))


if __name__ == "__main__":
    main()
