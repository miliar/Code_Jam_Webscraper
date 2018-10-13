#!/usr/bin/python2
# -*- coding: utf-8 -*-

import sys
import os

rl = sys.stdin.readline
def rs():
    return rl().split()

def ri():
    return int(rl())

def rvi():
    return map(int, rs())

def emptyright(a, i, j):
    for x in a[i][j+1:]:
        if x != ".":
            return False
    return True

def emptybot(a, i, j):
    for k in xrange(i+1, len(a)):
        if a[k][j] != ".":
            return False
    return True

def emptyleft(a, i, j):
    for x in a[i][:j]:
        if x != ".":
            return False
    return True

def emptytop(a, i, j):
    for k in xrange(0, i):
        if a[k][j] != ".":
            return False
    return True

def solve(a):
    r = 0
    for i in xrange(len(a)):
        c = 0
        one = -1
        for j, x in enumerate(a[i]):
            if x != '.':
                c += 1
                one = j
        if c == 1:
            c = 0
            for j in xrange(len(a)):
                if a[j][one] != '.':
                    c += 1
            assert c >= 0
            if c == 1:
                return "IMPOSSIBLE"

    for i in xrange(len(a)):
        for j in xrange(len(a[0])):
            c = a[i][j]
            if c == '^':
                if not emptytop(a, i, j):
                    continue
            elif c == 'v':
                if not emptybot(a, i, j):
                    continue
            elif c == '<':
                if not emptyleft(a, i, j):
                    continue
            elif c == '>':
                if not emptyright(a, i, j):
                    continue
            else:
                continue
            r += 1


    return r
    

def main():
    T = ri()
    for t in xrange(1, T+1):
        R, C = rvi()
        a = []
        for r in xrange(R):
            a.append(rl().strip())
        print "Case #%d: %s" % (t, str(solve(a)))


if __name__ == '__main__':
    main()
