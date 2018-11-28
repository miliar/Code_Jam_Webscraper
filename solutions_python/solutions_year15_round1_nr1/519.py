#!/usr/bin/env python
# vim:fileencoding=utf-8

import sys
import pprint

pp = pprint.PrettyPrinter(indent=4)

ntest = 0
inputs = []

def first_method(xs):
    lastx = xs[0]
    acc = 0
    for x in xs[1:]:
        diff = lastx - x
        if diff > 0:
            acc += diff
        lastx = x

    return acc

def second_method(xs):
    rate = 0
    lastx = xs[-1]
    for x in xs[::-1][1:]:
        rate = max(rate, x - lastx)
        lastx = x

    acc = 0

    for x in xs[:-1]:
        if rate > x:
            acc += x
        else:
            acc += rate
    return acc

def solve():
    for t in range(ntest):
        xs = inputs[t]["xs"]
        n = inputs[t]["n"]

        first = first_method(xs)
        second = second_method(xs)

        print "Case #{0}: {1} {2}".format(t + 1, first, second)

def parse():
    global ntest
    global inputs
    ntest = int(sys.stdin.readline().strip())
    for t in range(ntest):
        n = sys.stdin.readline().strip()
        xs = sys.stdin.readline().strip().split()
        xs = [int(x) for x in xs]
        inputs.append({"xs": xs, "n": n})
    # pp.pprint(inputs)

if __name__ == '__main__':
    parse()
    solve()
