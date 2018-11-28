#!/usr/bin/env python3

import sys

def cookie_time(rate, cost, delta, target):
    """
    Calculate the best time to reach target
    """

    # Conver the rate in float to avoid funny rounding errors
    rate = float(rate)
    t = 0.0
    best = 2.0*target/rate
    while t<best:
        # We have 2 options:
        # a) Go for the target
        # b) Build a farm and start again with better rate
        time_to_x = t + target/rate
        best = min(best, time_to_x)
        t += cost/rate
        rate += delta
    return best


def solve(fd):
    """
    Read all the cases and write the solution to stdout
    """
    T = int(fd.readline().strip())

    rate0 = 2.0

    for k in range(T):
        c, f, x = [float(s) for s in fd.readline().strip().split()]
        
        sol = cookie_time(rate0, c, f, x)

        print("Case #{}: {:.7f}".format(k+1, sol))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        infile = sys.stdin
    else:
        infile = open(sys.argv[1], 'r')

    solve(infile)

    infile.close()
