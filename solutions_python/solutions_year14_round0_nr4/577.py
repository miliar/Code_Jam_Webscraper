#!/bin/env python

def print_case(n, s):
    print("Case #%d: %s" % (n, s))

def deceitful(naomi, ken):
    naomi = sorted(naomi)
    ken = sorted(ken)
    t = 0
    for w in naomi:
        if w > ken[0]:
            ken.remove(ken[0])
            t += 1
        else:
            ken.pop()
    return t

def optimally(naomi, ken):
    naomi = sorted(naomi, reverse=True)
    ken = sorted(ken, reverse=True)
    t = 0
    for w in naomi:
        if w > ken[0]:
            ken.pop()
            t += 1
        else:
            ken.remove(ken[0])
    return t


def solve(n):
    raw_input()
    naomi = [float(i) for i in raw_input().split(' ')]
    ken = [float(i) for i in raw_input().split(' ')]
    deceit = deceitful(naomi, ken)
    opt = optimally(naomi, ken)
    print_case(n, "%d %d" % (deceit, opt))


if __name__ == '__main__':
    N = int(raw_input())
    for i in range(N):
        solve(i + 1)
