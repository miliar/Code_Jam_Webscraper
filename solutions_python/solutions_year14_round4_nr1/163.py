#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

nbcases = int(raw_input())

sys.setrecursionlimit(10000)

def nbmini(capacity, tailles):
    compteur = 0
    while (len(tailles) > 0):
        compteur += 1
        plusgros = tailles[0]
        tailles.remove(plusgros)
        for t in tailles:
            if (t+plusgros <= capacity):
                tailles.remove(t)
                break
    return compteur


for case in xrange(1,nbcases+1):
    [n,capacity] = [eval (n) for n in raw_input().strip().split(" ")]
    tailles = [eval(n) for n in raw_input().strip().split(" ")]
    tailles.sort(reverse=True)

    print "Case #%d: %d" % (case,nbmini(capacity,tailles))

