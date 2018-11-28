#!/usr/bin/env python3

# This code jam solution is powered by Nathan West's LibCodeJam; see
# https://github.com/Lucretiel/LibCodeJam for source code and (ostensibly) some
# documentation.

from code_jam import *

import math
import pprint
from collections import deque

# import code_jam; code_jam.INSERT_NEWLINE = True

# quick reference:
#   @autosolve, @collects, @cases(n)gen ... yield from gen
#   tokens.token(t), tokens.many(n, t)
#   debug(expr), @unroll(t)gen
#   solve(
#       int_token: int,
#       list_token: ('int_token', str),
#       set_token: (None, float, set)  # get a fresh int token for the length
#   ):


def num_servings(recipe, package):
    lower = 0.9 * recipe
    upper = 1.1 * recipe

    upper_servings = math.floor(package / lower)
    lower_servings = math.ceil(package / upper)

    return set(range(lower_servings, upper_servings+1))


@autosolve
@collects
def solve(
    num_ingredients: int,
    num_packages: int,
    recipe: ('num_ingredients', int),
    packages: ('num_ingredients * num_packages', int),
):
    grouped_packages = [sorted(packages[i:i+num_packages]) for i in range(0, len(packages), num_packages)]
    processed_packages = [
        deque(filter(None, (num_servings(amount, package) for package in package_list)))
        for amount, package_list in zip(recipe, grouped_packages)
    ]

    num_kits = 0

    debug(packages)

    while all(processed_packages):
        attempt = set.intersection(*(package[0] for package in processed_packages))
        if attempt:
            num_kits += 1
            for packages in processed_packages:
                del packages[0]
        else:
            target = max(min(packages[0]) for packages in processed_packages)
            for packages in processed_packages:
                if target not in packages[0]:
                    del packages[0]


    return num_kits

