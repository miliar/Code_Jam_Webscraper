#!/usr/bin/env python

from collections import deque

def get_optimal_score(block_cnt, blocks_a, blocks_b):
    blocks_a = deque(blocks_a)
    blocks_b = deque(blocks_b)
    score = 0
    while block_cnt > 0:
        if blocks_a[-1] < blocks_b[-1]:
            blocks_a.popleft()
            blocks_b.pop()
        else:
            blocks_a.pop()
            blocks_b.pop()
            score += 1
        block_cnt -= 1

    return score


def solve(lines):
    block_cnt = int(lines[0].strip())
    blocks_naomi = [float(n) for n in lines[1].split()]
    blocks_ken   = [float(n) for n in lines[2].split()]

    blocks_naomi.sort()
    blocks_ken.sort()

    return get_optimal_score(block_cnt, blocks_naomi, blocks_ken), \
            block_cnt - get_optimal_score(block_cnt, blocks_ken, blocks_naomi)

    
import sys
#import pdb

if __name__ == '__main__':
    filename_prefix = sys.argv[1]
    filename_in = filename_prefix + ".in"
    filename_out = filename_prefix + ".out"

    with open(filename_in, 'r') as file_in:
        lines = file_in.readlines()

    testcnt = int(lines[0])
    idx = 1

    with open(filename_out, 'w') as file_out:
        #pdb.set_trace()
        for test in range(testcnt):
            res = solve(lines[idx:idx+3])
            file_out.write("Case #%d: %d %d\n" % (test + 1, res[0], res[1]))
            idx += 3
