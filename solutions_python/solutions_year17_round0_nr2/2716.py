# -*- coding: utf-8 -*-
import sys

inp = sys.stdin

inp = open("B.in")

__author__ = "Filip Koprivec"


def solve(num: str) -> str:
    data = list(map(int, reversed(num)))
    res = [data[0]]
    N = len(data)
    for j in range(1, N):
        if data[j] > data[j - 1]:
            for i in range(j):
                data[i] = 9
            #data[j - 1] = 9
            data[j] = data[j] - 1
    if data[-1] == 0:
        return "9" * (N - 1)
    return "".join(map(str, reversed(data)))


def main():
    N = int(inp.readline())
    outfile = open("B-Small.out", "w")
    #outfile = sys.stdout
    for j in range(N):
        k = inp.readline().strip()
        res = solve(k)

        print("Case #{num}:".format(num=j + 1), res, file=outfile)


if __name__ == '__main__':
    main()
