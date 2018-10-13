#!/usr/bin/env python3

import sys


def main():
    lines = sys.stdin.readlines()
    n = int(lines[0])
    for case, line in enumerate(lines[1:n+1]):
        case += 1
        start, k = line.split()
        k = int(k)
        value = 0
        if k > len(start):
            print("Case #%d: IMPOSSIBLE" % case)
            continue
        target = 2**len(start) - 1
        for i in start:
            value = value << 1
            if i == "+":
                value += 1
        flipper = 2**k - 1
        i = 0
        flips = 0
        while value != target:
            if not value & 1 << i:
                value ^= flipper
                flips += 1
            flipper = flipper << 1
            i += 1
            if i > len(start) - k:
                break
        if value == target:
            print("Case #%d: %d" % (case, flips))
        else:
            print("Case #%d: IMPOSSIBLE" % case)


if __name__ == "__main__":
    main()
