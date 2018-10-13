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

class FlipError(Exception): pass

def Pancakes(rep):
    return [True if p == '+' else False for p in rep]

def flip(pancakes, index, length):
    front, back = index, index + length

    if back > len(pancakes):
        raise FlipError()

    pancakes[front:back] = [not p for p in pancakes[front:back]]

@autosolve
@collects
def solve(pancakes: Pancakes, length: int):
    flips = 0
    index = 0
    try:
        while True:
            index = pancakes.index(False)
            flip(pancakes, index, length)
            flips += 1
    except ValueError:
        return flips
    except FlipError:
        return 'IMPOSSIBLE'
