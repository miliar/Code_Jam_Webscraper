#!/usr/bin/env python
# encoding: utf-8

from __future__ import division

import sys

from itertools import takewhile

def counter():
    n = 0
    while True:
        yield n
        n += 1

def strategy(cand, i):
    c = filter(lambda x: x > i, cand)
    if c:
        c_min = min(c)
    else:
        c_min = min(cand)
    return c_min

def war(naomi_mood, ken_mood):
    normal_war_ken_mood = list(ken_mood)
    naomi_score_normal = 0
    for i in naomi_mood:
        c = strategy(normal_war_ken_mood, i)
        if i > c:
            naomi_score_normal += 1
        #print i, c
        #print "*****"
        normal_war_ken_mood.remove(c)

    cheat_war_naomi_mood = list(reversed(naomi_mood))
    naomi_score_cheat = 0
    for i in reversed(ken_mood):
        c = cheat_war_naomi_mood[0]
        if c > i:
            cheat_war_naomi_mood.remove(c)
            naomi_score_cheat += 1
        else:
            cheat_war_naomi_mood.pop()
    return naomi_score_cheat, naomi_score_normal

def main():
    times = int(sys.stdin.readline())
    for case_n in xrange(1, times+1):
        total = int(sys.stdin.readline())
        naomi_mood = sorted(map(float, sys.stdin.readline().split()))
        ken_mood = sorted(map(float, sys.stdin.readline().split()))
        #print "====================="
        print "Case #%d:" % case_n, "%d %d" % war(naomi_mood, ken_mood)

if __name__ == "__main__":
    main()
