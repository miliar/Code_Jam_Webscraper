#!/usr/bin/python2
# -*- coding: utf-8 -*-

import sys

def rl(proc=None):
    if proc is not None:
        return proc(sys.stdin.readline())
    else:
        return sys.stdin.readline().rstrip()

def srl(proc=None):
    if proc is not None:
        return map(proc, rl().split())
    else:
        return rl().split()

def solve(s, n):
    s = [x == '+' for x in s]
    count = 0
    for i in xrange(len(s) - n + 1):
        if not s[i]:
            for j in xrange(n):
                s[i+j] = not s[i+j]
            count += 1
    if all(s[len(s) - n + 1:]):
        return count
    else:
        return "IMPOSSIBLE"

def main():
    T = rl(int)
    for t in xrange(1, T+1):
        s, n = srl()
        print "Case #%d: %s" % (t, solve(s, int(n)))

if __name__ == '__main__':
    main()
