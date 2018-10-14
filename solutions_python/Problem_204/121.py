import functools as ft
import itertools as it
import numpy as np
from math import *
import decimal


def solve(recipe, packs):
    recipe = list(map(decimal.Decimal, recipe))
    packs_new = []
    for p in packs:
        packs_new.append(list(map(decimal.Decimal, p)))
    packs = packs_new
    def check(ps):
        kit_n = ps[0]
        if kit_n > 0: # sufficient and same mult
            max_guess = ceil(kit_n * (decimal.Decimal(1.1) / decimal.Decimal(.9)))
            min_guess = floor(kit_n * (decimal.Decimal(.9) / decimal.Decimal(1.1)))
            for kit in range(min_guess, max_guess + 1):
                if all([abs(act - kit) <= decimal.Decimal(.1) * kit for act in ps]):
                    return True
        return False

    # Transform in kits proportions
    # Sort
    proportions = []
    for prop, line in zip(recipe, packs):
        proportions.append(sorted([p / prop for p in line]))

    # Transform recipe to 1
    recipe = [1 for _ in recipe]

    checker = lambda x: all([len(l) > 0 for l in x])

    i = 0
    while checker(proportions):
        col1 = [x[0] for x in proportions]
        if check(col1):
            i += 1
            proportions = [l[1:] for l in proportions]
        else:
            mini = min(col1)
            for j,k in enumerate(col1):
                if k == mini:
                    break
            proportions[j] = proportions[j][1:]

    return i





if __name__ == '__main__':
    for qq in range(1, int(input())+1):
        line = input().split()
        N, P = map(int, line)
        recipes = map(int, input().split())
        xs = []
        for _ in range(N):
            xs.append(map(int, input().split()))
        ans = solve(recipes, xs)
        print('Case #{}: {}'.format(qq, ans))

