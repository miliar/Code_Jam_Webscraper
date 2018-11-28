#!/usr/bin/python2
# -*- coding: utf-8 -*-

import sys

def rl(proc=None):
    if proc is not None:
        return proc(sys.stdin.readline())
    else:
        return sys.stdin.readline().rstrip()

def solve(N):
    prev = '9'
    br = None
    for i, c in enumerate(reversed(N)):
        if c > prev:
            br = i
            prev = chr(ord(c) - 1)
        else:
            prev = c
    if br is None:
        return N
    br = len(N) - 1 - br
    return N[:br] + chr(ord(N[br])-1) + '9' * (len(N) - br - 1)

def main():
    T = rl(int)
    for t in xrange(1, T+1):
        N = rl()
        print "Case #%d: %s" % (t, solve(N).lstrip("0"))

if __name__ == '__main__':
    main()
