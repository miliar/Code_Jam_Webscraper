from __future__ import division
from math import floor, ceil
from sys import stdin, stdout
from collections import defaultdict

def get_servings(qty, recipe_amt):

    min_servings = int(ceil(qty / (recipe_amt * 1.1)))
    max_servings = int(floor(qty / (recipe_amt * 0.9)))

    return frozenset(range(min_servings, max_servings + 1))

def pick_package(package_list, servings):
    best = None
    for pkg in package_list:
        if servings in pkg:
            if (best == None) or (min(pkg) > min(best)):
                best = pkg

    return best


def solve(packages, num_ingr, max_servings):
    num_kits = 0
    servings = max_servings
    while servings:
        best_pkgs = []
        for ingr in range(num_ingr):
            best_pkgs.append(pick_package(packages[ingr], servings))

        if any(pkg == None for pkg in best_pkgs):
            servings -= 1
            continue

        for ingr in range(num_ingr):
            packages[ingr].remove(best_pkgs[ingr])

        num_kits += 1

    return num_kits

T = int(stdin.readline())

for t in range(T):
    num_ingr, num_pack = map(int, stdin.readline().strip().split())
    recipe = map(int, stdin.readline().strip().split())

    packages = []
    max_servings = 0
    for ingr in range(num_ingr):
        packages.append([])
        for pkg in map(int, stdin.readline().strip().split()):
            servings = get_servings(pkg, recipe[ingr])
            if servings:
                max_servings = max(max_servings, max(servings))
                packages[ingr].append(servings)

    result = solve(packages, num_ingr, max_servings)

    stdout.write("Case #{}: {}\n".format(t+1, result))