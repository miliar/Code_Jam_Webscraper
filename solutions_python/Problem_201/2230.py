#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import heapq


def main():
    for case in range(int(sys.stdin.readline().strip())):
        n, k = map(int, sys.stdin.readline().strip().split())
        h = [-n]
        for _ in range(k):
            t = -heapq.heappop(h)
            spaces = t
            heapq.heappush(h, -(t // 2))
            heapq.heappush(h, -((t - 1) // 2))
        print(
            'Case #{}: {} {}'.format(case + 1, spaces // 2, (spaces - 1) // 2))


if __name__ == '__main__':
    main()
