#!/usr/bin/env python
# vim: set filetype=python et sw=4 ts=4:

import sys
sys.setrecursionlimit(1024*1024)

T = int(sys.stdin.readline())

def solve():
    N = int(sys.stdin.readline())
    naomi = [float(x) for x in sys.stdin.readline().split()]
    ken = [float(x) for x in sys.stdin.readline().split()]
    naomi.sort()
    ken.sort()
    sys.stdout.write("%d %d" %
                (play_deceitful_war(naomi, ken), play_war(naomi, ken)))

def play_war(naomi, ken):
    score = 0
    naomi = list(naomi)
    ken = list(ken)

    while len(naomi):
        val = naomi.pop(0)
        kens_point = False
        for i, kval in enumerate(ken):
            if kval > val:
                ken.pop(i)
                kens_point = True
                break
        if not kens_point:
            ken.pop(0)
            score += 1

    return score

def play_deceitful_war(naomi, ken):
    score = 0
    naomi = list(naomi)
    ken = list(ken)

    naomi.reverse()
    ken.reverse()

    while len(naomi) > 0:

        kens_point = False
        if naomi[0] > ken[0]:
            # we want ken to use his largest block here for our smalles
            if len(naomi) > 1:
                told = ken[0] - 0.0000001
            else:
                told = naomi[0]
            val = naomi.pop(0)
        else:
            # we want him to use his largest block
            val = naomi.pop()
            told = ken[0] - 0.0000001

        for i, kval in enumerate(ken):
            if kval > val: 
                ken.pop(i)
                kens_point = True
                break
        if not kens_point:
            ken.pop(0)
            score += 1
    return score

for case in xrange(T):
    sys.stdout.write("Case #%d: " % (case + 1))
    solve()
    sys.stdout.write("\n")
