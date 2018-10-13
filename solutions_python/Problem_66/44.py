#!/usr/bin/env python
import copy
import fileinput
inp= fileinput.input()

def megasplit(prices):
    p1, p2 = [], []

    for thing in prices:
        l = len(thing)/2
        p1.append(thing[:l])
        p2.append(thing[l:])

    return p1, p2

def solve(i, j, p, m, prices):
    if p < 1:
        return 0
    lim = len(m)/2
    c = 0 
    k = i + j/2

    price = prices.pop()[0]
    # custo assistindo
    if max(m) > 0:
        m2 = [max(0, x-1) for x in m]
        p1, p2 = megasplit(prices)
        c = solve(i, k, p-1, m2[:lim], p1) + solve(k+1, j, p-1, m2[lim:], p2) + price
    # custo sem assistir
    if max(m) < p:
        p1, p2 = megasplit(prices)
        c2 = solve(i, k, p-1, m[:lim], p1) + solve(k+1, j, p-1, m[lim:], p2)
        c = min(c, c2)

    return c


def go():
    p = int(inp.readline())
    m = map(int, inp.readline().split())
    m = [(p-x) for x in m]
    prices = []
    for i in xrange(p):
        prices.append(map(int, inp.readline().split()))

    return solve(0, p-1, p, m, prices)
    pass

if __name__ == "__main__":
    t = int(inp.readline())
    for i in xrange(1, t+1):
        print 'Case #%d: %d' % (i, go())
    
