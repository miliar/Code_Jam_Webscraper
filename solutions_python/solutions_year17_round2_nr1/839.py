#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def solve(cipher):
    m = -sys.maxint
    horses = []
    D, N = map(int, cipher.split())
    for i in range(N):
        horses.append(map(int, raw_input().split()))
    for horse in horses:
        num = float(D-horse[0])/horse[1]
        m = max(m, num)
    return D/m

if __name__ == "__main__":
    testcases = input()

    for caseNr in xrange(1, testcases+1):
        cipher = raw_input()
        print("Case #%i: %s" % (caseNr, solve(cipher)))
