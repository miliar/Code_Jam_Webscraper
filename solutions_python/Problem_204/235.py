import math
import itertools

f_in = open('B-small-attempt0.in')
f_out = open('Bsmall.out', 'w')

T = int(f_in.readline())

def rintlist():
    return [int(z) for z in f_in.readline().rstrip().split()]

def usable(packages, q):
    ret = []  # (amt, [servings])
    lower_bound = q * 0.9
    upper_bound = q * 1.1
    for p in packages:
        # divide by upper and lower bound of ingredient amount
        # find amount of servings you can make with the lower and upper bounds...
        min_amount = int(math.ceil(p / upper_bound))
        max_amount = int(p / lower_bound)

        if min_amount <= max_amount:
            # the range is valid
            ret.append((p, (min_amount, max_amount)))
        # otherwise, you can't make any legal amount of servings.
        # (if theres one legal possible amount of servings, min == max -
        #  if theres multiple, everything in range min -> max inclusive is legal)
    return ret

def solve():
    N, P = rintlist()
    rat = rintlist()
    # print N, P, rat   # ingredients, packages of each, recipe
    ingredient_packages = []
    for i in range(N):
        # Discard any packages that can never be used (not within 90-110% of a serving size)
        packages = rintlist()
        ingredient_packages.append(usable(packages, rat[i]))

    if N == 1:
        return len(ingredient_packages[0])

    else:
        # bruteforce!!!
        best = 0
        for perm in itertools.permutations(range(len(ingredient_packages[1]))):
            ok = 0
            lensecond = len(ingredient_packages[1])
            for i, first in enumerate(ingredient_packages[0]):
                if i >= lensecond:
                    break
                second = ingredient_packages[1][perm[i]]
                # check if ranges overlap
                if first[1][1] >= second[1][0] and second[1][1] >= first[1][0]:
                    ok += 1
                    # print first, second
            if ok >= best:
                best = ok

        return best


for case in range(1, T+1):
    out = 'Case #{}: {}\n'.format(case, solve())
    f_out.write(out)
    print out



f_in.close()
f_out.close()
