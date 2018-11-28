#!/usr/bin/env python

import sys

def play_war(naomi, ken):
    naomi_points = 0
    while naomi:
        naomi_play = naomi.pop(0)
        winning = [k for k in ken if k > naomi_play]
        if winning:
            ken.remove(min(winning))
        else:
            ken.pop(0)
            naomi_points += 1
    return naomi_points

def play_deceit(naomi, ken):
    naomi_points = 0
    while naomi:
        if naomi[0] < ken[0]:
            naomi.pop(0)
            ken.pop()
        else:
            naomi.pop(0)
            ken.pop(0)
            naomi_points += 1
    return naomi_points

if __name__ == "__main__":
    games = []
    with open(sys.argv[1]) as f:
        n = int(f.readline().strip())
        for _ in range(n):
            f.readline()
            naomi = sorted([float(i) for i in f.readline().strip().split()])
            ken = sorted([float(i) for i in f.readline().strip().split()])
            games.append((naomi, ken))

    points = []
    for g in games:
        naomi = g[0]
        ken = g[1]
        points.append((play_deceit(naomi[:], ken[:]), play_war(naomi[:], ken[:])))


    for i, (d, w) in enumerate(points, start=1):
        print("Case #%d: %d %d" % (i, d, w))
