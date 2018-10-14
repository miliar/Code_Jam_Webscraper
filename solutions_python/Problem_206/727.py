#!/usr/local/bin/python3

import logging

def solve(problem):
    D, horses = problem
    t = max((D - k) / s for (k, s) in horses)
    return D / t

def parse_problems():
    import fileinput
    fin = fileinput.input()

    T = int(next(fin))
    for _ in range(T):
        D, N = list(map(int, next(fin).split()))
        horses = [tuple(map(int, next(fin).split())) for i in range(N)]
        yield D, horses

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
