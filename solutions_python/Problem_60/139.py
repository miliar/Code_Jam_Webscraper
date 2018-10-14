#!/usr/bin/env python
#-*- encoding: utf-8 -*-

# chick :
# 0 -> pos
# 1 -> speed

from operator import itemgetter

def time_needed_without_swap(chick, barn_pos):
    dist = barn_pos - chick[0]
    return float(dist) / float(chick[1])

def candidates(chick, barn_pos, K, T):
    chick = [(time_needed_without_swap(ch, barn_pos), ch)
             for ch in chick]
    chick = [(p, s) for (t, (p, s)) in chick if t <= T]
    chick.sort(reverse=True)
    return chick[:K]

if __name__ == '__main__':
    C = input()
    for c in xrange(1, C+1):
        N, K, B, T = [int(x) for x in raw_input().split()]
        locs = [float(x) for x in raw_input().split()]
        speeds = [float(x) for x in raw_input().split()]
        chicks = [(locs[i], speeds[i]) for i in xrange(N)]
        cands = candidates(chicks, B, K, T)

        if len(cands) < K:
            print 'Case #%d: IMPOSSIBLE' % c
            continue

        swaps = 0
        for i, (p1, s1) in enumerate(chicks):
            if (p1, s1) not in cands:
                continue
            for (p2, s2) in chicks[i+1:]:
                if (p2, s2) not in cands:
                    swaps += 1
        print 'Case #%d: %d' % (c, swaps)
