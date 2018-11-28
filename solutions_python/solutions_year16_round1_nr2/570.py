#!/usr/bin/env python3

import sys
import math

def rank_and_file(n, heights):
    counts = {}
    for row_col in heights:
        for h in row_col:
            if h not in counts:
                counts[h] = 1
            else:
                counts[h] += 1
    missing = []
    for h, count in counts.items():
        if count % 2 == 1: # Odd
            missing.append(h)
    return sorted(missing)

def main():
    if len(sys.argv) < 2:
        print("Usage: rank_and_file.py <file>")
        exit()
    in_file = sys.argv[1]
    with open(in_file) as f:
        cases = int(f.readline())
        for i in range(0, cases):
            n = int(f.readline().strip()) # Strip off the newline
            heights = []
            for j in range(0, 2*n - 1):
                row_col = [int(h) for h in f.readline().strip().split()]
                heights.append(row_col)
            print("Case #%d: %s" % (i+1, " ".join([str(h) for h in rank_and_file(n, heights)])))

##########

if __name__ == '__main__':
    main()
