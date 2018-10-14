#!/usr/bin/env python2.7

T = int(raw_input())
for x in xrange(1, T + 1):
    M = int(raw_input()) - 2
    EN = set(raw_input().split())
    FR = set(raw_input().split())
    BOTH = EN & FR
    EN -= BOTH
    FR -= BOTH
    words = [set(raw_input().split()) - BOTH for i in xrange(M)]
    subsets = []
    subsets.append(set())
    for j in xrange(1, 1 << M):
        k = (j - 1) & j
        subsets.append(subsets[k] | words[len(bin(j ^ k)) - 3])
    res = 1e9
    for j in xrange(1 << M):
        en = EN | subsets[j]
        fr = FR | subsets[(1 << M) - j - 1]
        res = min(res, len(en & fr))
    print 'Case #{}: {}'.format(x, res + len(BOTH))
