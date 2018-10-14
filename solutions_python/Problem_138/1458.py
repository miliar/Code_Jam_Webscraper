#!/usr/bin/python3

import sys

t = int(sys.stdin.readline())

def war(naomi_, ken_):
    naomi = naomi_[:]
    ken = ken_[:]
    points = 0
    while len(naomi) > 0:
        n = naomi.pop(0) # heaviest
        if ken[0] < n:
            # naomi wins
            points += 1
            del ken[-1]
        else:
            # ken wins
            i = 0
            while i+1 < len(ken) and ken[i+1] > n:
                i += 1
            del ken[i]
    return points

def deceitful_war(naomi_, ken_):
    naomi = naomi_[:]
    ken = ken_[:]
    points = 0
    pos = len(naomi) - 1
    for i in range(len(ken)-1, -1, -1):
        # can we destroy i'th?
        # print('Can we destroy %f?' % ken[i])
        while pos > 0 and naomi[pos] < ken[i]:
            pos -= 1
        if naomi[pos] > ken[i]:
            points += 1
            # print('Yes, with %f!' % naomi[pos])
            pos -= 1
        if pos < 0:
            break
    return points

for case_num in range(1, t+1):
    n = int(sys.stdin.readline())
    naomi = list(reversed(sorted(map(float, sys.stdin.readline().split()))))
    ken = list(reversed(sorted(map(float, sys.stdin.readline().split()))))
    # print(naomi)
    # print(ken)
    d = deceitful_war(naomi, ken)
    w = war(naomi, ken)
    print("Case #%d: %d %d" % (case_num, d, w))