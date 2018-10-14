#!/usr/bin/env python3

# This code jam solution is powered by Nathan West's LibCodeJam; see
# https://github.com/Lucretiel/LibCodeJam for source code and (ostensibly) some
# documentation.

from code_jam import *
from heapq import heappush, heappop, heappushpop, heapreplace
from collections import Counter

# import code_jam; code_jam.INSERT_NEWLINE = True

# quick reference:
#   @autosolve, @collects, @cases(n)gen ... yield from gen
#   tokens.token(t), tokens.many(n, t)
#   debug(expr), @unroll(t)gen
#   solve(
#       int_token: int,
#       list_token: ('int_token', str),
#       set_token: (None, float, set)  # get a fresh int token for the length
#   ):

def partition(length):
    length2 = length - 1
    left_chunk = length2 // 2
    right_chunk = length2 - left_chunk
    return left_chunk, right_chunk

@autosolve
@collects
def solve(num_stalls: int, num_people: int):
    queue = [-num_stalls]
    counts = Counter([num_stalls])

    while True:
        size = heappop(queue)
        size = -size
        count = counts[size]
        del counts[size]

        left, right = partition(size)
        num_people -= count
        if num_people <= 0:
            return right, left

        if left == right:
            if counts[left] == 0:
                heappush(queue, -left)
            counts.update({left: count * 2})
        else:
            if counts[left] == 0:
                heappush(queue, -left)
            if counts[right] == 0:
                heappush(queue, -right)
            counts.update({left: count, right: count})

