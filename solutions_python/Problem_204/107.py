#!/usr/bin/env python3

from math import floor, ceil

def form(recipe, packages):
    N = len(recipe)
    for Qi in packages:
        Qi.sort()
    pack = [iter(Qi) for Qi in packages]
    cur = [-1]*N
    kits = 0
    n = 0 # number of servings
    while True:
        for i,c in enumerate(cur):
            Ri = recipe[i]
            while c < ceil(Ri*n*0.9):
                c = next(pack[i], None)
                if c is None: return kits
            cur[i] = c
            if floor(Ri*n*1.1) < c:
                while floor(Ri*n*1.1) < c:
                    n += 1
                break
        else:
            cur = [-1]*N
            kits += 1


import sys
file=sys.stdin

n = int(file.readline()) # number of cases
for case in range(1, n+1):
    N, P = map(int, file.readline().split())
    recipe = [int(Ri) for Ri in file.readline().split()]
    packages = []
    for i in range(N):
        packages.append([int(Qj) for Qj in file.readline().split()])

    ans = form(recipe, packages)

    print("Case #%d: %d" % (case, ans))
