#!/usr/bin/env python3

import math


T = int(input())
for i in range(T):
    (C, F, X) = map(float, input().split())
    n = max(0, math.ceil((X * F - C * F - 2 * C) / (C * F)))
    t = X / (2 + n * F) + sum([C / (2 + j * F) for j in range(n)])
    print("Case #{}: {}".format(i + 1, t))
