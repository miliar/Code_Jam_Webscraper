#!/usr/bin/env python
# -*- coding utf-8 -*-

import sys
import math

def check(K, N):
    space = K - N

    depth = math.floor(math.log2(N+1))+1
    if 2**(depth-1) == N+1:
        depth -= 1
    leafsp = 2 ** (depth-1)

    if N == leafsp + 1:
        x = (space // leafsp)
        if space % leafsp == 0:
            return x//2 + x%2, x//2
        else:
            x += 1
            return x//2 + x%2, x//2
    else:
        x = (space // leafsp)
        return x//2 + x%2, x//2



T = int(sys.stdin.readline().strip())
c = 1
while True:
    l = sys.stdin.readline()
    if l == "":
        break
    K, N = map(int, l.strip().split(" "))

    ma, mi = check(K, N)

    print("Case #%d: %d %d" % (c, ma, mi))

    c += 1
