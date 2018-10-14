#!/usr/bin/env python

import sys

def calc_for_idx(idx, k, g, themap):
    lg = len(g)
    if idx not in themap:
        val = 0
        c = 0
        cidx = idx 
        while (val + g[cidx] <= k) and (c < lg):
            val += g[cidx]
            cidx = (cidx + 1) % lg
            c += 1
        themap[idx] = (val, cidx) 
    return themap[idx]


def go(r, k, g):
    themap = {}
    curr = 0
    monies = 0
    for i in xrange(r):
        (luc, nex) = calc_for_idx(curr, k, g, themap)
        #print "run #%d: %d" % (i+1, luc)
        monies += luc
        curr = nex

    return monies


if __name__ == '__main__':
    import fileinput
    inp = fileinput.input()

    T = int(inp.readline())

    for t in xrange(1, T+1):
        r, k, n = map(int, inp.readline().split())
        g = map(int, inp.readline().split())
        print "Case #%d: %d" % (t, go(r, k, g))
