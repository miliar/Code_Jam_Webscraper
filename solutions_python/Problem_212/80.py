#!/usr/bin/env python

from operator import itemgetter

def solve():
    N, P = [int(i) for i in raw_input().split()]
    groups = {i: 0 for i in xrange(P)}
    for i in raw_input().split():
        groups[int(i) % P] += 1
    sol = groups[0]
    groups[0] = 0
    for i in xrange(1, (P+1)/2):
        n = min(groups[i], groups[P - i])
        sol += n
        groups[i] -= n
        groups[P - i] -= n
    if P % 2 == 0:
        sol += groups[P/2]/2
        groups[P/2] -= 2 * (groups[P/2] / 2)
    k, v = max(groups.iteritems(), key=itemgetter(1))
    if (P == 4) and (groups[2] != 0):
        if v > 2:
            sol += 1
            groups [2] == 0
            groups [k] -= 2
    if v > 0:
        sol += v/P + (v % P > 0)
    return sol


def main():
    T = int(raw_input())
    for i in xrange(T):
        sol = solve()
        print 'Case #{}: {}'.format(i+1, sol)


if __name__ == '__main__':
    main()
