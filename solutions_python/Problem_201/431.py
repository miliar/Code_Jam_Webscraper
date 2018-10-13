#!/usr/local/bin/python3

import logging
from collections import Counter
import heapq

def solve(problem):
    N, K = problem
    assert K <= N
    counter = Counter()
    heap = []

    def estimate(block_size):
        lr_min = (block_size - 1) // 2
        lr_max = (block_size    ) // 2
        return lr_min, lr_max

    def push(block_size, n):
        lr_min, lr_max = estimate(block_size)
        if counter[block_size] == 0:
            heapq.heappush(heap, (-lr_min, -lr_max, block_size))
        counter[block_size] += n

    def pop():
        _, _, block_size = heapq.heappop(heap)
        n = counter[block_size]
        counter[block_size] = 0
        return block_size, n

    push(N, 1)
    while True:
        block_size, n = pop()
        lr_min, lr_max = estimate(block_size)
        # logging.info("{} -> {} + {} (x{})".format(block_size, lr_min, lr_max, n))
        if K <= n:
            return "{} {}".format(lr_max, lr_min)
        K -= n
        if lr_min > 0:
            push(lr_min, n)
        if lr_max > 0:
            push(lr_max, n)

def parse_problems():
    import fileinput
    fin = fileinput.input()

    T = int(next(fin))
    for _ in range(T):
        yield map(int, next(fin).split())

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
