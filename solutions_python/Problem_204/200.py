# 0th solution to Problem B

from math import floor
from itertools import combinations_with_replacement
from itertools import permutations


# n ingredients
# p packages of each ingredient

# s[i] of ith ingredient in the recipe for 1 serving
# ings [i][j] in the jth package of ith ingredient
# ings2[i][j] stores (min_servings, max_servings for jth package of ith ingredient
# i < n, j < p

t = int(input())
for a0 in range(t):
    res = None
    n, p = map(int, input().strip().split(' '))
    s = list(map(int, input().strip().split(' ')))
    ings = []
    ings2 = []
    for a1 in range(n):
        ings.append(list(map(int, input().strip().split(' '))))

    for i, ing in enumerate(ings):
        ings2.append([])
        for pack in ing:
            min_servings = None
            max_servings = None
            min_amount = 0.9 * s[i]
            max_amount = 1.1 * s[i]
            servings = floor(pack/max_amount)
            while pack >= servings * min_amount:
                if pack <= servings * max_amount:
                    if min_servings is None:
                        min_servings = servings
                    max_servings = servings
                servings += 1
            ings2[-1].append((min_servings, max_servings))

    #print("ings", ings)
    #print()
    #print("ings2", ings2)

    if n == 1:
        res = 0
        for rrange in ings2[0]:
            if rrange[0] is not None:
                res += 1

    elif n == 2:
        res = 0
        for perm in permutations(list(range(p)), p):
            this_res = 0
            for i, x in enumerate(perm):
                if ings2[0][i][0] is None or ings2[1][x][0] is None:
                    continue
                if (ings2[0][i][0] <= ings2[1][x][1] and ings2[0][i][0] >= ings2[1][x][0]):
                    this_res += 1
                elif (ings2[1][x][0] <= ings2[0][i][1] and ings2[1][x][0] >= ings2[0][i][0]):
                    this_res += 1
            if this_res > res:
                res = this_res

    else:
        for choice in combinations_with_replacement(list(range(p)), n):
            failed = False
            minn, maxx = None, None
            res_here = 0
            for ing, p_num in enumerate(choice):
                if ings2[ing][p_num][0] is None:
                    failed = True
                    continue
                else:
                    min_here, max_here = ings2[ing][p_num]
                    if minn is None:
                        minn, maxx = min_here, max_here
                    else:
                        minn = max(minn, min_here)
                        maxx = min(maxx, max_here)
                        if minn > maxx:
                            failed = True
                            break

            if failed:
                continue
            if res is None:
                pass


    print("Case #" + str(a0 + 1) + ": " + str(res))
