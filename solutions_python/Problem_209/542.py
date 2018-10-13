#!/usr/local/bin/python3

import logging
import math

def max_k_sum(nums, K):
    assert K >= 1
    N = len(nums)
    sums = [0] * (N + 1)
    for k in range(K - 1):
        sums_ = [0] * (N + 1)
        for i in range(N - 1 - k, -1, -1):
            sums_[i] = max(sums_[i + 1], sums[i + 1] + nums[i])
        sums = sums_
    return [sums[i + 1] + n for (i, n) in enumerate(nums)]

def solve(problem):
    K, pancakes = problem
    N = len(pancakes)
    pancakes = sorted(pancakes, reverse=True)
    side_area_sums = max_k_sum([2 * r * h for r, h in pancakes], K)
    best = max(r * r + side_area_sums[i] for i, (r, h) in enumerate(pancakes))
    return math.pi * best

def parse_problems():
    import fileinput
    fin = fileinput.input()

    T = int(next(fin))
    for _ in range(T):
        N, K = list(map(int, next(fin).split()))
        pancakes = [tuple(map(int, next(fin).split())) for i in range(N)]
        yield K, pancakes

def main():
    import time
    logging.basicConfig(level=logging.INFO, format="%(message)s")

    t0 = time.time()
    logging.info("Starting...")
    for i, p in enumerate(parse_problems()):
        ans = solve(p)
        logging.info("Solved #%d", i + 1)
        print("Case #{}: {}".format(i + 1, ans))
    logging.info("Finished in %.2f s", time.time() - t0)

if __name__ == '__main__':
    main()
