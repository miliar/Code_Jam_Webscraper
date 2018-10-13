# -*- coding: utf-8 -*-
import sys

inp = sys.stdin

inp = open("A.in")

from typing import Optional

__author__ = "Filip Koprivec"


def solve(panc: str, k: int) -> Optional[int]:
    data = [j == "-" for j in panc]
    N = len(data)
    flips = 0
    flippings = set()  # should use queue, but works well enough
    for j in range(N - k + 1):
        try:
            flippings.remove(j)
        except KeyError:
            pass
        if (data[j] + len(flippings)) % 2:  # flip
            flips += 1
            flippings.add(j + k)
    for j in range(N - k + 1, N):
        try:
            flippings.remove(j)
        except KeyError:
            pass
        if (data[j] + len(flippings)) % 2:
            return None
    return flips


def main():
    N = int(inp.readline())
    outfile = open("A-Small.out", "w")
    for j in range(N):
        panc, k = inp.readline().split()
        res = solve(str(panc), int(k))
        ans = "IMPOSSIBLE" if res is None else str(res)
        print("Case #{num}:".format(num=j + 1), ans, file=outfile)


if __name__ == '__main__':
    main()
