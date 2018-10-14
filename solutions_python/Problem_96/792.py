#!/usr/bin/env python

import math
import sys
import itertools
from pprint import pprint

def break_score(n, S):
    if n == 0: return 0

    if S > 0: g = 2 if n % 3 > 1 else 1
    else:     g = 1 if n % 3 > 0 else 0

    return math.floor(n / 3) + g

def max_score(p, rest, permute):
    mx = 0

    for i in range(len(rest)):
        score = rest[i]
        sm = break_score(score, permute[i])
        #print('score: %d, sm: %d, S: %d' % (score, sm, S))
        if sm >= p: mx += 1

    return mx

def googlers():
    count = int(sys.stdin.readline())

    for i in range(count):
        line = sys.stdin.readline().strip()
        nums = list(map(int, line.split()))
        N = nums[0]
        S = nums[1]
        p = nums[2]
        rest = sorted(nums[3:])
        mx = 0

        s_orders = [1] * S + [0] * (N-S)
        for s_permute in itertools.permutations(s_orders):
            a = max_score(p, rest, s_permute)
            if a > mx: mx = a

        #print('rest: %s, N: %d, S: %d, p: %d' % (rest, N, S, p))
        print('Case #%d: %s' % (i+1, mx))

    #pprint(db)
    #pprint(tr(sample[0][0], db))


if __name__ == '__main__':
    googlers()
