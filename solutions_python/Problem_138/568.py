#!/usr/bin/env python3

T = int(input())
for case in range(1, T+1):
    N = int(input())
    naomi = dict.fromkeys((float(x) for x in input().split()), 1)
    ken = dict.fromkeys((float(x) for x in input().split()), -1)
    blocks = naomi
    blocks.update(ken)
    points = [[blocks[x], True] for x in sorted(blocks)]

    deceitful_wars = 0
    current_point = 0
    for j in reversed(points):
        if j[1]:
            current_point += j[0]
            if j[0] == 1 and current_point > 0:
                deceitful_wars += 1
            elif current_point < 0:
                current_point += 1
                for k in points:
                    if k == [1, True]:
                        k[1] = False
                        break

    normal_wars = 0
    current_point = 0
    for j in reversed(points):
        current_point += j[0]
        if normal_wars < current_point:
            normal_wars = current_point

    print('Case #{0}: {1} {2}'.format(case, deceitful_wars, normal_wars))
