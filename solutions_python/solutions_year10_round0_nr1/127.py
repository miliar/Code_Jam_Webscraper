#! /usr/bin/env python
# -*- coding: utf-8 -*-

from sys import stdin

count = int(stdin.readline().strip())
for i in range(count):
    N, K = map(int, stdin.readline().strip().split())
    if (K + 1) % (2 ** N) == 0:
        result = "ON"
    else:
        result = "OFF"
    print("Case #{0}: {1}".format(i + 1, result))
