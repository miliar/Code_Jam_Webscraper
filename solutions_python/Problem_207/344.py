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

def max_skip(seq, index):
    max_val = float("-inf")
    max_index = None

    for i, v in enumerate(seq):
        if i != index:
            if v > max_val:
                max_val = v
                max_index = i

    return max_index

color_table = ['R', 'Y', 'B']

@autosolve
@collects
def solve(N: int, R: int, O: int, Y: int, G: int, B: int, P: int):
    assert O == G == P == 0

    for pop in R, Y, B:
        if pop * 2 > N:
            return "IMPOSSIBLE"

    colors = {
        'R': R,
        'Y': Y,
        'B': B
    }

    priority_seq = sorted(
        ['R', 'Y', 'B'],
        key=lambda c: colors[c],
        reverse=True
    )

    prev = None

    sequence = []

    def max_skip():
        max_pop = 0
        max_color = None

        for color in priority_seq:
            if color != prev:
                if colors[color] > max_pop:
                    max_pop = colors[color]
                    max_color = color

        return max_color

    for i in range(N):
        max_color = max_skip()
        colors[max_color] -= 1
        sequence.append(max_color)
        prev = max_color

    return ''.join(sequence)
