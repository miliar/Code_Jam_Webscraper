#!/usr/local/bin/python3

import logging

def digits2num(digits):
    n = 0
    for d in digits:
        n = 10 * n + d
    return n

def solve(digits):
    L = len(digits)
    i0, d0 = 0, digits[0]
    while i0 < L: 
        for i1 in range(i0 + 1, L):
            d1 = digits[i1]
            if d0 == d1:
                continue
            if d1 > d0:
                i0, d0 = i1, d1
                break
            digits[i0] = d0 - 1
            for j in range(i0 + 1, L):
                digits[j] = 9
            return digits2num(digits)
        else:
            break
    return digits2num(digits)

def parse_problems():
    import fileinput
    fin = fileinput.input()

    T = int(next(fin))
    for _ in range(T):
        digits = list(map(int, next(fin).strip()))
        yield digits

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
