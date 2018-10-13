#!/usr/bin/env python3

import numpy as np
import itertools

def main():
    T = int(input())
    for t in range(1, T + 1):
        D, N = list(map(int, input().split()))
        data = []
        for i in range(N):
            Ki, Si = list(map(int, input().split()))
            data.append((Ki, Si))
        times = []
        for (Ki, Si) in data:
            times.append((D - Ki) / Si)
        sol = D / max(times)
        print("Case #" + str(t) + ": " + str(sol))


if __name__ == "__main__":
    main()
