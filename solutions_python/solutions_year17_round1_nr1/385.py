# coding: utf-8

import os, sys, re, string
import math,random

def draw(cakes, x, y, r, c, ch):
    sx, ex = x, x
    sy, ey = y, y
    for j in xrange(x + 1, c):
        if cakes[y][j] != '?':
            break
        ex = j
    for j in xrange(x - 1, -1, -1):
        if cakes[y][j] != '?':
            break
        sx = j
    loop_break = False
    for i in xrange(y + 1, r):
        for j in xrange(sx, ex + 1):
            if cakes[i][j] != '?':
                loop_break = True
                break
        if loop_break:
            break
        ey = i
    loop_break = False
    for i in xrange(y - 1, -1, -1):
        for j in xrange(sx, ex + 1):
            if cakes[i][j] != '?':
                loop_break = True
                break
        if loop_break:
            break
        sy = i
    #print "found {0}  ({1},{2}) => ({3}, {4})".format(ch, sx, sy, ex, ey)
    for i in xrange(sy, ey + 1):
        for j in xrange(sx, ex + 1):
            cakes[i][j] = ch


def solve(cakes, r, c):
    used = {}
    for y in xrange(r):
        for x in xrange(c):
            ch = cakes[y][x]
            if ch == '?' or ch in used:
                continue
            used[ch] = True
            draw(cakes, x, y, r, c, ch)

def main():
    t = int(sys.stdin.readline())
    for x in xrange(1, t + 1):
        r, c = map(int, sys.stdin.readline().split(' '))
        cakes = map(lambda x: map(lambda s: s, sys.stdin.readline().strip()), xrange(r))
        print "Case #{0}: ".format(x)
        solve(cakes, r, c)
        print "\n".join(map(lambda row: "".join(row), cakes))


if __name__ == '__main__':
    main()


