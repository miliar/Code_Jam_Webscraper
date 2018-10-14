#!/usr/bin/env python3

import os
from heapq import heappush, heappop


def main(n, k):
    if n == k:
        return [0, 0]

    heap = [-n]
    for _ in range(k):
        max_item = -heappop(heap)
        max_item = max_item - 1
        i = max_item // 2
        j = max_item - i
        heappush(heap, -i)
        heappush(heap, -j)
    return sorted([i, j], reverse=True)


if __name__ == '__main__':
    with open(os.path.expanduser("~/Downloads/C-small-1-attempt0.in")) as fd:
        t = int(fd.readline())
        for i in range(1, t + 1):
            n, k = map(int, fd.readline().strip().split())
            r = main(n, k)
            print("Case #{}: {} {}".format(i, *r))
