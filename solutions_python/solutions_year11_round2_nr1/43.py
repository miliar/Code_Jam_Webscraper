#!/usr/bin/pypy
# -*- coding: utf-8 -*-

import sys
import os
from pprint import pprint

def wp(line):
    return float(line.count('1'))/(line.count('1') + line.count('0'))

def WP(schedule):
    return map(wp, schedule)

def getopps(line):
    return [i for i,v in enumerate(line) if v != '.']

def OWP(schedule):
    ret = []
    for i,line in enumerate(schedule):
        opps = getopps(line)
        s = 0.0
        n = 0
        for o in opps:
            s += wp(schedule[o][:i] + schedule[o][i+1:])
            n += 1
        ret.append(s/n)
    return ret

def OOWP(schedule, _owp):
    ret = []
    for i,line in enumerate(schedule):
        opps = getopps(line)
        s = 0.0
        n = 0
        for o in opps:
            s += _owp[o]
            n += 1
        ret.append(s/n)
    return ret

def solve(schedule):
    _wp = WP(schedule)
    _owp = OWP(schedule)
    _oowp = OOWP(schedule, _owp)
    #pprint(_wp)
    #pprint(_owp)
    #pprint(_oowp)
    ret = []
    for x, y, z in zip(_wp,_owp,_oowp):
        ret.append(0.25 * x + 0.50 * y + 0.25 * z)
    return ret

def main():
    T = int(sys.stdin.readline())
    for i in xrange(1, T+1):
        N = int(sys.stdin.readline())
        schedule = []
        for j in xrange(N):
            schedule.append(sys.stdin.readline().strip())
        print "Case #" + str(i) + ":"
        print "\n".join(map(str,solve(schedule)))

if __name__ == '__main__':
    main()
