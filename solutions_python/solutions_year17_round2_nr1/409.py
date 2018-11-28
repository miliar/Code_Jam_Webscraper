#!/usr/bin/env python3

# This code jam solution is powered by Nathan West's LibCodeJam; see
# https://github.com/Lucretiel/LibCodeJam for source code and (ostensibly) some
# documentation.

from code_jam import *

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


def arrival_time(D, K, S):
    distance = D - K
    return (D-K) / S


@autosolve
@collects
def solve(D: int, horses: (None, (int, int))):
    t = max(arrival_time(D, *horse) for horse in horses)
    return D / t
