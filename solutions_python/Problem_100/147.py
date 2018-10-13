#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
T = int(sys.stdin.readline())
for t in range(1, T+1):
    N = int(sys.stdin.readline())
    A = [None] * N
    B = [None] * N
    for i in range(N):
        A[i], B[i] = tuple([int(x) for x in sys.stdin.readline().split(None)])
    # search
    cand = set([tuple([0] * (N + 2))]) # level1, level2, ..., num of stars, num of cleared 2-star
    num_plays = 1
    cleared = False
    while True:
        tmp = set()
        # 2-star
        for c in cand:
            # play a game
            for i in range(N):
                # can he play the i-th level for 2-star rating?
                if c[i] <= 1 and c[N] >= B[i]:
                    # OK
                    lst = list(c)
                    if c[i] == 1:
                        lst[i] += 1
                        lst[N] += 1
                    else:
                        lst[i] += 2
                        lst[N] += 2                        
                    lst[N+1] += 1 # num of 2-star
                    tmp.add(tuple(lst))
                    if lst[N+1] == N:
                        # cleared!
                        print "Case #%d: %d" % (t, num_plays)
                        cleared = True
                        break
            if cleared:
                break
        if cleared: 
            break

        # 1-star
        if len(tmp) == 0:
            for c in cand:
                # play a game
                for i in range(N):
                    # can he play the i-th level for 1-star rating?
                    if c[i] == 0 and c[N] >= A[i]:
                        # OK
                        lst = list(c)
                        lst[i] += 1
                        lst[N] += 1 # 1-star rating
                        tmp.add(tuple(lst))

        if len(tmp) == 0:
            # Too Bad!
            print "Case #%d: Too Bad" % (t)
            break
        num_plays += 1
        cand = tmp
