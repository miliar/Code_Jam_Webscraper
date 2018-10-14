#!/usr/bin/env python3

import random

def best_rock(played_rock, deck):
    for i, rock in enumerate(deck):
        if rock > played_rock:
            return i
    return 0

def war(naomi, ken):
    n_rocks = len(naomi)
    score_n = score_k = 0
    for _ in range(n_rocks):
        rock_n = naomi.pop(random.randint(0, len(naomi)-1))
        rock_k = ken.pop(best_rock(rock_n, ken))
        if rock_n > rock_k:
            score_n += 1
        else:
            score_k +=1
        #print("-> %f vs %f [%d/%d]" % (rock_n, rock_k, score_n, score_k))
        #print(naomi)
        #print(ken)
        assert len(naomi) == len(ken)
    return score_n

def deceitful_war(naomi, ken):
    n_rocks = len(naomi)
    score_n = score_k = 0
    for _ in range(n_rocks):
        if naomi[0] > ken[0]:
            naomi.pop(0)
            ken.pop(0)
            score_n += 1
        else:
            naomi.pop(0)
            ken.pop()
            score_k += 1
    return score_n


T = int(input())
for t in range(1, T+1):
    _ = int(input())
    naomi = sorted(map(float, input().split()))
    ken = sorted(map(float, input().split()))
    best = "x"

    print("Case #%d: %d %d" % (
        t, 
        deceitful_war(list(naomi), list(ken)),
        war(list(naomi), list(ken))))
