#!/usr/bin/env python

import sys
import math

def solve(stalls, people):
    a = [stalls]
    for c in range(people):
        i = a.index(max(a))
        l = math.floor(a[i]/2)
        r = math.ceil(a[i]/2) - 1
        a = a[0:i] + [l] + [r] + a[i+1:]

    return l, r


def main(infile):
    with open(infile, 'r') as f:
        T = f.readline()

        case = 1
        for line in f:
            s = list(map(int, line.split(' ')))
            l, r = solve(s[0], s[1])
            print("Case #{}: {} {}".format(case, l, r))
            case = case + 1

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
