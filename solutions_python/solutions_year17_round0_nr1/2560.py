#!/usr/bin/env python
# vim:fileencoding=utf-8

import sys
import pprint

pp = pprint.PrettyPrinter(indent=4)

ntest = 0
inputs = []


def solve():
    for t in range(ntest):
        K = inputs[t]["K"]
        cakes = inputs[t]["cakes"]

        nflip = 0
        ncake = len(cakes)
        # print(cakes)
        for i in range(ncake - K + 1):
            # print(i, cakes)
            if cakes[i] == 0:
                nflip += 1
                for j in range(K):
                    cakes[i + j] = 1 - cakes[i + j]  # flip

        # print(cakes)
        # print(ncake, sum(cakes))
        result = nflip if sum(cakes) == ncake else "IMPOSSIBLE"

        print("Case #{0}: {1}".format(t + 1, result))


def parse():
    global ntest
    global inputs
    ntest = int(sys.stdin.readline().strip())
    for n in range(ntest):
        line = sys.stdin.readline().strip()
        cakes_str, K = line.split()
        K = int(K)
        cakes = [1 if c == "+" else 0 for c in cakes_str]
        inputs.append({"cakes": cakes, "K": K})
    #pp.pprint(inputs)


if __name__ == '__main__':
    parse()
    solve()
