# -*- coding: utf-8 -*-
from itertools import chain

# This library is available online and free to use:
# https://github.com/yanatan16/pycodejam
from codejam.parsers import iter_parser

# Input
#
# 6
# XXXT
# ....
# OO..
# ....
#
# XOXT
# XXOO
# OXOX
# XXOO
#
# XOX.
# OX..
# ....
# ....
#
# OOXX
# OXXX
# OX.T
# O..O
#
# XXXO
# ..O.
# .O..
# T...
#
# OXXX
# XO..
# ..O.
# ...O

# Output
#
# Case #1: X won
# Case #2: Draw
# Case #3: Game has not completed
# Case #4: O won
# Case #5: O won
# Case #6: O won


def solve(*lines):
    # return lines
    size = 4
    x_set = ('X', 'T')
    y_set = ('O', 'T')
    for s in (x_set, y_set):
        # rows
        for i in xrange(size):
            # print lines[4 * i:4 * i + 4]
            if all(char in s for char in lines[4 * i:4 * i + 4]):
                return '{} won'.format(s[0])
        # cols
        for i in xrange(size):
            # print lines[i::4]
            if all(char in s for char in lines[i::4]):
                return '{} won'.format(s[0])
        # diagonals
        diag1 = [lines[size * i + i] for i in xrange(size)]
        # print diag1
        if all(char in s for char in diag1):
            return '{} won'.format(s[0])
        diag2 = [lines[size * i + size - i - 1] for i in xrange(size)]
        # print diag2
        if all(char in s for char in diag2):
            return '{} won'.format(s[0])
    if any(char == '.' for char in lines):
        return "Game has not completed"
    return "Draw"


def iter_wrap(f):
    def wrap():
        return list(f())
    return wrap


@iter_parser
def parse(nxtline):
    # blank line & 4 lines
    nxtline = iter_wrap(nxtline)
    case_lines = 3
    first_line = nxtline()
    case = [nxtline() for unused in xrange(case_lines)]
    if not first_line:
        case.append(nxtline())
    else:
        case.insert(0, first_line)
    return reduce(lambda x, y: x + y, case)

if __name__ == "__main__":
    from codejam import CodeJam
    # import ipdb; ipdb.set_trace()
    CodeJam(parse, solve).main()
