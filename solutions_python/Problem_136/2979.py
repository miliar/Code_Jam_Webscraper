#!/usr/bin/env python
# vim:fileencoding=utf-8

import sys
import pprint

pp = pprint.PrettyPrinter(indent=4)

ntest = 0
inputs = []

def solve():
    for n in range(ntest):
        c = inputs[n][0]
        f = inputs[n][1]
        x = inputs[n][2]

        cps = 2
        t = 0

        while True:
            complete_t = x / cps
            buy_t = c / cps
            predict_t = x / (f + cps)
            if complete_t > buy_t + predict_t:
                t += buy_t
                cps += f
            else:
                t += complete_t
                break

        print "Case #{0}:".format(n+1),
        print t

def parse():
    global ntest
    global inputs
    ntest = int(sys.stdin.readline().strip())
    for n in range(ntest):
        inputs.append([float(x) for x in sys.stdin.readline().strip().split()])
    # pp.pprint(inputs)

if __name__ == '__main__':
    parse()
    solve()
