import sys
import os
import math
from collections import defaultdict

from tqdm import tqdm

fin = open('C-large.in.txt')
# fin = open('B-large.in.txt')
# fout = sys.stdout
fout = open('out_1_large', 'w')


def solve(n, k):
    mem    = defaultdict(int)
    mem[n] = 1

    while k > 0:
        max_key = max(mem.keys())
        val = mem[max_key]
        if val < k:
            k -= val
            mem[max_key / 2] += val
            mem[max(0, (max_key - 1) / 2)] += val

            del mem[max_key]
        else:
            return max_key / 2, max(0, (max_key - 1) / 2)

    max_key = max(mem.keys())
    return max_key / 2, max(0, (max_key - 1) /  2)


if __name__ == '__main__':
    count = int(fin.readline().strip())

    for i in range(count):
        line = fin.readline().strip().split()
        n, k = map(int, line)
        result = solve(n, k)
        fout.write('Case #%s: %s %s\n' % ((i + 1, ) + result))


