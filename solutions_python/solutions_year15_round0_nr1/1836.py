#!/usr/bin/env python
# vim:fileencoding=utf-8

import sys
import pprint

pp = pprint.PrettyPrinter(indent=4)

ntest = 0
inputs = []

def solve():
    for t in range(ntest):
        n = inputs[t]["n"]
        num_needs = inputs[t]["num_needs"]
        nfriend = 0
        nstands = 0
        for i, j in enumerate(num_needs):
            if nstands >= i:
                nstands += j
            else:
                nfriend += i - nstands
                nstands += j + i - nstands

        print "Case #{0}: {1}".format(t + 1, nfriend)


def parse():
    global ntest
    global inputs
    ntest = int(sys.stdin.readline().strip())
    for n in range(ntest):
        line = sys.stdin.readline().strip()
        num_needs = []
        n, needs_str = line.split()
        n = int(n)
        for i in range(n + 1):
            num_needs.append(int(needs_str[i]))
        inputs.append({"num_needs": num_needs, "n": n})
    # pp.pprint(inputs)

if __name__ == '__main__':
    parse()
    solve()
