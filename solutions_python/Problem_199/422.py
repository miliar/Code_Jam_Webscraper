#!/usr/local/bin/python3

import logging

def solve(problem):
    cakes, K = problem
    def swap(pos):
        for i in range(pos, pos + K):
            cakes[i] = -cakes[i]
    ans = 0
    for pos in range(len(cakes)):
        if cakes[pos] == 1:
            continue
        try:
            swap(pos)
            ans += 1
        except IndexError as e:
            return "IMPOSSIBLE"
    return ans

def parse_problems():
    import fileinput
    fin = fileinput.input()

    T = int(next(fin))
    for _ in range(T):
        cakes, K = next(fin).split()
        yield list(map(lambda s: s == "+" and 1 or -1, cakes)), int(K)

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
