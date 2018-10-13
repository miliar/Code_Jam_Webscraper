import math
import itertools

def solve(recipe, ingredients):
    limits = transform(recipe, ingredients)
    count = 0
    if len(recipe) == 1:
        return len(limits[0])
    if len(recipe) != 2:
        return None
    for pairing in itertools.permutations(range(len(ingredients[0]))):
        potential_count = 0
        for i, pair in enumerate(pairing):
            if i >= len(limits[0]) or pair >= len(limits[1]):
                continue
            (min_1, max_1) = limits[0][i]
            (min_2, max_2) = limits[1][pair]
            if min_1 > max_2 or min_2 > max_1:
                continue
            potential_count += 1
        if potential_count > count:
            count = potential_count
    return count

def faster_solve(recipe, ingredients):
    limits = transform(recipe, ingredients)
    pointers = [0 for i in range(len(limits))]

    count = 0
    while True:
        if pointers[0] >= len(limits[0]):
            return count
        (lower, upper) = limits[0][pointers[0]]
        success = True
        max_limiter = 0
        for i in range(1, len(limits)):
            if pointers[i] >= len(limits[i]):
                return count
            (new_lower, new_upper) = limits[i][pointers[i]]
            while new_upper < lower and pointers[i] < len(limits[i]) - 1:
                pointers[i] += 1
                new_lower, new_upper = limits[i][pointers[i]]
            if pointers[i] >= len(limits[i]) or new_upper < lower:
                return count
            if new_lower > upper:
                pointers[max_limiter] += 1
                success = False
                break
            lower = max(lower, new_lower)
            if new_upper < upper:
                upper = new_upper
                max_limiter = i
        if success:
            count += 1
            for i in range(len(limits)):
                pointers[i] += 1

    return count


def transform(recipe, ingredients):
    limits = []
    for i, ingredient in enumerate(ingredients):
        ingredient_limits = []
        for package in ingredient:
            factor = float(package) / recipe[i]
            lower_bound = int(math.ceil(factor / 1.1))
            upper_bound = int(math.floor(factor / 0.9))
            if lower_bound > upper_bound:
                continue
            else:
                ingredient_limits.append((lower_bound, upper_bound))
        limits.append(sorted(ingredient_limits))
    return limits




def parse():
    N, P = [int(i) for i in raw_input().split()]
    recipe = [int(i) for i in raw_input().split()]
    ingredients = []
    for r in range(N):
        row = [int(c) for c in raw_input().split()]
        ingredients.append(row)
    return recipe, ingredients

T = int(raw_input())
for t in range(1, T+1):
    recipe, ingredients = parse()
    print("Case #{0}: {1}".format(t, faster_solve(recipe, ingredients)))