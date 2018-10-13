import copy
import heapq
import sys

_cache = {}

def solve_problem(num_diners, diners):
    _key = tuple(sorted(diners))
    if _key in _cache:
        return _cache[_key]

    if not diners:
        return 0

    heapq._heapify_max(diners)
    maxelem = heapq.heappop(diners)

    if maxelem < 3:
        return maxelem

    res = []
    for i in xrange(maxelem / 2 + 1):
        next_diners = copy.copy(diners)
        next_diners.append(maxelem - i)
        if i != 0:
            next_diners.append(maxelem - (maxelem - i))
        if i == 0:
            next_diners = filter(None, map(lambda x: x - 1, next_diners))
        res.append(1 + solve_problem(num_diners, next_diners))

    result = min(res)
    _cache[_key] = result

    return result


if __name__ == "__main__":
    num_of_cases = int(sys.stdin.readline().strip())

    for i in xrange(1, num_of_cases + 1):
        num_diners = int(sys.stdin.readline().strip())
        diners = map(int, sys.stdin.readline().split())
        print "Case #{0}: {1}".format(i, solve_problem(num_diners, diners))
