from collections import deque
from itertools import product
from functools import lru_cache, reduce

@lru_cache(None)
def interval(n, k):
    r = set()
    # This function is terrible.
    for x in range((n*10)//(k*11), (n*10)//(k*9)+2):
        if k*x*9 <= n*10 <= k*x*11:
            r.add(x)

    return r

@lru_cache(None)
def valid_package(R, package):
    ranges = reduce(set.__and__, [interval(n, k) for n, k in zip(package, R)])
    return bool(ranges)


def solve2(packages, seen, min_index):
    if not packages:
        return 0

    m = 0
    for i in range(min_index, len(packages)):
        package = packages[i]
        if package & seen:
            continue

        r = solve2(packages[:i] + packages[i+1:], package | seen, i) + 1
        m = max(m, r)

    return m


def solve(R, packages):
    valid_packages = []
    for x in product(*[range(len(p)) for p in packages]):
        package = [p[i] for i, p in zip(x, packages)]
        if valid_package(tuple(R), tuple(package)):
            valid_packages.append(set(enumerate(x)))

    r = solve2(valid_packages, set(), 0)
    return r


with open('B-small-attempt1.in') as infile:
    with open('B-small-attempt1.out', 'w') as outfile:
        cases = int(next(infile))

        for case in range(1, cases+1):
            N, P = map(int, next(infile).split())
            R = list(map(int, next(infile).split()))
            packages = []

            for _ in range(N):
                packages.append(list(map(int, next(infile).split())))

            result = solve(R, packages)
            print("Case #{}: {}".format(case, result), file=outfile)
            print(case, result)

