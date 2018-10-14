#!/usr/bin/python2
# -*- coding: utf-8 -*-

import sys
import os

def subsolve(x,v,R,t):
    xv = zip(x,v)
    xv.sort(key = lambda p: p[1])
    ret = 0.0
    for x,v in xv:
        dt = float(x)/(v+R)
        if t < 1e-9:
            ret += float(x)/v
        elif dt < t:
            t -= dt
            ret += dt
        else:
            walk = x - (v+R) * t
            ret += t + float(walk)/v
            t = 0.0

    return ret


def solve(X,S,R,t,w):
    c = 0
    R -= S
    x = []
    v = []
    for b,e,s in w:
        if b > c:
            x.append(b-c)
            v.append(S)
        x.append(e-b)
        v.append(S+s)
        c = e
    if (c < X):
        x.append(X-c)
        v.append(S)
    return subsolve(x,v,R,t)

def main():
    T = int(sys.stdin.readline())
    for _t in xrange(1, T+1):
        X, S, R, t, N = map(int,sys.stdin.readline().split())
        w = []
        for i in xrange(N):
            w.append(map(int,sys.stdin.readline().split()))
        print "Case #" + str(_t) + ": " + ("%17.17f" % solve(X,S,R,t,w))

if __name__ == '__main__':
    main()
