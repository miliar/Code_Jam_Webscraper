#!/usr/bin/env python
#coding=utf-8


def unique(row):
    first = row[0] if row[0] != 'T' else row[1]
    if first not in ['X', 'O']:
        return None
    for e in row:
        if e != first and e!= 'T':
            return None
    return first


def find_row(game):
    result = None
    for row in game:
        result = unique(row)
        if result:
            return result + ' won'
    return result


def find_col(game):
    result = None
    for i in xrange(len(game[0])):
        result = unique([r[i] for r in game])
        if result:
            return result + ' won'
    return result


def find_diag(game):
    d1 = []
    d2 = []
    n = len(game)
    for i in xrange(n):
        d1.append(game[i][i])
        d2.append(game[n-1-i][i])
    result = unique(d1)
    if not result:
        result = unique(d2)
    if result:
        return result + ' won'
    else:
        return None


def find_dot(game):
    for row in game:
        for c in row:
            if c == '.':
                return 'Game has not completed'
    return None


def solve(game):
    result = find_row(game)
    if not result:
        result = find_col(game)
    if not result:
        result = find_diag(game)
    if not result:
        result = find_dot(game)
    if not result:
        return "Draw"
    else:
        return result


def solve_cases(games):
    """
    parsed_input = [[input1], ]
    """
    result = []
    for i, game in enumerate(games):
        result.append("Case #%s: " % (i+1) + solve(game))
    return result

import argparse
from parser_codejam import AbstractParser


class Parser(AbstractParser):
    def parse_line(self, line):
        return line

if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument("input", action="store")

    args = argparser.parse_args()
    results = solve_cases(Parser(input_path=args.input).parse())
    for result in results:
        print result
