#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

def flip(cakes, start, size):
    for i in xrange(start, start+size):
        cakes[i] = '-' if cakes[i] == '+' else '+'

def solve(c, s):
    times = 0
    size = int(s)
    cakes = list(c)
    for i in xrange(len(cakes) - size + 1):
        if cakes[i] == '-':
            flip(cakes, i, size)
            times += 1
    for i in xrange(len(cakes) - size + 1, len(cakes)):
        if cakes[i] == '-':
            return "IMPOSSIBLE"
    return times

if __name__ == "__main__":
    T = input()
    for t in xrange(1, T+1):
        cakes, size = map(str ,sys.stdin.readline().split())
        print "Case #{no}: {result}".format(no=t, result=solve(cakes, size))
