# -*- coding: utf-8 -*-
def print_ans(case, y):
    print 'Case #%d:' % case, y


def stand_up(standing, levels):
    p = standing
    standing += levels[standing]
    while p < standing and p < len(levels) - 1:
        p += 1
        standing += levels[p]
    return standing


def get_y(levels):
    standing = 0
    a = sum(levels)
    y = 0

    standing = stand_up(standing, levels)

    while standing != a:
        y += 1
        a += 1
        standing += 1
        standing = stand_up(standing, levels)

    return y


T = int(raw_input().strip())

for t in xrange(T):
    sMax, levels = raw_input().strip().split()
    sMax = int(sMax.strip())

    levels = [int(l) for l in levels.strip()]

    y = get_y(levels)

    print_ans(t + 1, y)
