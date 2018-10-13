#!/usr/bin/env python3

# This code jam solution is powered by Nathan West's LibCodeJam; see
# https://github.com/Lucretiel/LibCodeJam for source code and (ostensibly) some
# documentation.

from code_jam import *
from gridly import Grid

import code_jam

code_jam.INSERT_NEWLINE = True

# quick reference:
#   @autosolve, @collects, @cases(n)gen ... yield from gen
#   tokens.token(t), tokens.many(n, t)
#   debug(expr), @unroll(t)gen
#   solve(
#       int_token: int,
#       list_token: ('int_token', str),
#       set_token: (None, float, set)  # get a fresh int token for the length
#   ):


class Cake(Grid):
    def __init__(self, rows):
        rows = list(rows)
        Grid.__init__(
            self,
            num_rows=len(rows),
            num_columns=len(rows[0]),
            func=lambda loc: rows[loc[0]][loc[1]])

    def __str__(self):
        return '\n'.join(''.join(row) for row in self.rows())


@autosolve
@collects
def solve(rows: int, columns: int, cake: ('rows', str, Cake)):
    begun = False
    for row_index, row in enumerate(map(list, cake.rows())):
        if all(cell == '?' for cell in row):
            if begun:
                for col_index, cell in enumerate(cake.row(row_index - 1)):
                    cake[row_index, col_index] = cell
        else:
            col_prefil = []
            current = None
            for col_index, cell in enumerate(row):
                if cell != '?':
                    current = cell
                    for col_index in col_prefil:
                        cake[row_index, col_index] = current
                    col_prefil = []
                else:
                    if current is None:
                        col_prefil.append(col_index)
                    else:
                        cake[row_index, col_index] = current
            if not begun:
                for col_index, cell in enumerate(cake.row(row_index)):
                    for old_index in range(row_index):
                        cake[old_index, col_index] = cell
                begun = True

    return cake
