#!/usr/bin/python

import sys


score_map = {0: (0, 0), 1: (1, 0), 2: (1, 2), 3: (1, 2), 4: (2, 2),
        5: (2, 3), 6: (2, 3), 7: (3, 3), 8: (3, 4), 9: (3, 4), 10: (4, 4),
        11: (4, 5), 12: (4, 5), 13: (5, 5), 14: (5, 6), 15: (5, 6),
        16: (6, 6), 17: (6, 7), 18: (6, 7), 19: (7, 7), 20: (7, 8),
        21: (7, 8), 22: (8, 8), 23: (8, 9), 24: (8, 9), 25: (9, 9),
        26: (9, 10), 27: (9, 10), 28: (10, 10), 29: (10, 11), 30: (10, 11)}


def calculate_best(score):
    ''' Calculate the max single score for this total, assuming
    surprising triplet and without it.'''

    mn = (score / 3) - 2
    mx = (score / 3) + 2

    if mn < 0:
        mn = 0
    if mx > 30:
        mx = 30

    best_sur = 0
    best = 0

    for a in range(mn, mx + 1):
        for b in range(mn, mx + 1):
            for c in range(mn, mx + 1):
                if a + b + c != score:
                    continue
                if abs(a - b) > 2 or abs(a - c) > 2 or abs(b - c) > 2:
                    continue
                if abs(a - b) == 2 or abs(a - c) == 2 or abs(b - c) == 2:
                    if max(a, b, c) > best_sur:
                        best_sur = max(a, b, c)
                else:
                    if max(a, b, c) > best:
                        best = max(a, b, c)

    return best, best_sur


def calculate_init():
    score_best_map = {}
    for score in range(0, 31):
        score_best_map[score] = calculate_best(score)

    print score_best_map


def max_googlers(scores, s, p):
    ans = 0
    for score in scores:
        if score_map[score][0] >= p:
            ans += 1
        elif score_map[score][1] >= p and s > 0:
            s -= 1
            ans += 1

    return ans


def max_googlers_init():
    t = int(sys.stdin.readline().strip())
    for i in range(1, t + 1):
        vals = [int(a) for a in sys.stdin.readline().strip().split()]
        ans = max_googlers(vals[3:], vals[1], vals[2])
        print 'Case #{0}: {1}'.format(i, ans)


max_googlers_init()
