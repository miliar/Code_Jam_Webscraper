import sys
from itertools import *
from collections import *
import math

def paintForNRings(r, n):
    first = r * 2 + 1
    last = first + (n - 1) * 4
    total = (first + last) * n / 2
    return n * total

def solve(f):
    r, t = map(int, next(f).split())

    def paintNeededForRing(r):
        return (r+1)**2 - r**2

    result = 0
    while paintNeededForRing(r) <= t:
        result += 1
        t -= paintNeededForRing(r)
        r += 2
    return result



def main(infile, outfile):
    with open(infile, 'r') as f:
        with open(outfile, 'w') as f2:
            cases = int(next(f))
            for i in range(cases):
                solution = solve(f)
                f2.write("Case #{}: {}\n".format(i+1, solution))

if __name__ == '__main__':
    main(*sys.argv[1:3])

