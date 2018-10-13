#!/usr/bin/env python3

# This code jam solution is powered by Nathan West's LibCodeJam; see
# https://github.com/Lucretiel/LibCodeJam for source code and (ostensibly) some
# documentation.

import itertools
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

def pairwise(it):
    a, b = itertools.tee(it)
    next(b, None)
    return zip(a, b)

def is_tidy(value):
    return all(a <= b for a, b in pairwise(map(int, str(value))))

@autosolve
@collects
def solve(value: int):
    while not is_tidy(value):
        val_str = str(value)
        head_str = val_str.rstrip('9')
        head_val = int(head_str[:-1])
        head_val -= 1
        new_val_str = str(head_val) + '9' * (len(val_str) - len(head_str) + 1)
        value = int(new_val_str)

    return value
