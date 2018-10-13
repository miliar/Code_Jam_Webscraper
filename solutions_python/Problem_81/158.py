#!/usr/bin/env python

import sys
import math
import random
import numpy


def solve():
    n = [int(x) for x in sys.stdin.readline().split()][0]
    s = []
    wp = []
    played = []
    won = []
    for i in xrange(n):
        s.append(sys.stdin.readline().strip())
        played.append(0)
        won.append(0)
        for c in s[-1]:
            if c != '.':
                played[-1] += 1
            if c == '1':
                won[-1] += 1
        wp.append(won[-1]*1.0/played[-1])
    owp = []
    for i in xrange(n):
        owp.append(0)
        for j,c in enumerate(s[i]):
            if c == '.': continue
            if s[j][i] == '0':
                owp[-1] += (won[j]*1.0/(played[j]-1) ) / played[i]
            elif s[j][i] == '1':
                owp[-1] += ((won[j]-1)*1.0/(played[j]-1) ) / played[i]

    ret = ""
    for i in xrange(n):
        ris = 0
        count = 0
        for j,c in enumerate(s[i]):
            if c != '.':
                count += 1
                ris += owp[j]
        ris /= count
        ris = 0.25*ris + 0.25*wp[i] + 0.5*owp[i]
        ret += "%.14lf\n" % ris
    return ret
    


def run():
    CCC = int(sys.stdin.readline())
    for CC in xrange(CCC):
        print "Case #" + str(CC+1) + ":"
        print solve(),

if __name__ == "__main__":
    run()




