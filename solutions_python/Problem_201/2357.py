#!/usr/bin/env python

import sys
import heapq


def bathroom(N, T):
    h = []
    heapq.heappush(h, -N)

    for _ in range(T - 1):
        c = abs(heapq.heappop(h)) - 1
        if c == 0:
            continue
        elif c == 1:
            heapq.heappush(h, -1)
            continue

        # c > 2
        half = c // 2
        heapq.heappush(h, -(half))
        if c % 2 == 0:
            heapq.heappush(h, -(half))
        else:
            heapq.heappush(h, -(half+1))

    current = abs(heapq.heappop(h)) - 1
    half = current // 2
    if current % 2 == 0:
        return half, half
    else:
        return half+1, half


def print_result(i, y, z):
    print("Case #{}: {} {}".format(i, y, z))


def main():
    a = int(sys.stdin.readline())
    for i in range(1, a + 1):
        line = sys.stdin.readline().split()
        N, T = int(line[0]), int(line[1])
        y, z = bathroom(N, T)
        print_result(i, y, z)


if __name__ == '__main__':
    main()
