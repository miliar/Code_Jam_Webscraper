#!/usr/bin/python

import sys

def memodict(f):
    """ Memoization decorator for a function taking a single argument """
    class memodict(dict):
        def __missing__(self, key):
            ret = self[key] = f(key)
            return ret
    return memodict().__getitem__

@memodict
def solve(ls):
    if len(ls) == 0:
        return 0
    sls = sorted(ls)
    highest = sls[-1]
    if highest == 1:
        return 1, "eat1"
    if highest == 2:
        return 2, "eat2"
    if highest == 3:
        return 3, "eat3"

    divides = [highest/3, highest/2]
    divideds = [sls[:-1] + [h, highest - h] for h in divides]

    plain_eat = max(ls)

    all_dscores = []
    for d in divideds:
        split_count, split_sol = solve(tuple(sorted(d)))
        split_cost = split_count + 1
        all_dscores.append((split_cost, d, split_sol))

    best_divided, d, best_sol = min(all_dscores, key=lambda c: c[0])

    min_cost = min(plain_eat, best_divided)
    if plain_eat == min_cost:
        return highest, "eat{}".format(highest)
    #elif eat_one_cost == min_cost:
    #    return eat_one_cost, "eat1{} >> ".format(eat_one) + eat_one_sol
    else:
        return best_divided, "split{} >> ".format(d) + best_sol


def run_it(text):
    tcs = text.split("\n")[1:]
    ls = [tcs[i+1].split() for i in range(0, len(tcs)-1, 2)]
    nls = [tuple(sorted(map(int, l))) for l in ls]

    return map(solve, nls)


def create_output(filename):
    with open(filename, "r") as fh:
        text = fh.read()

    results = run_it(text)
    output = "\n".join("Case #{}: {}".format(i+1, r[0]) for i, r in enumerate(
        results))
    with open("out_final.txt", "w+") as fh:
        fh.write(output)


create_output(sys.argv[1])
