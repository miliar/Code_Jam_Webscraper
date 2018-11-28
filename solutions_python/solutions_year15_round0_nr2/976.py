#! /usr/bin/env python -u
# coding=utf-8
import math
import sys

__author__ = 'xl'

move_dict = dict()


def solve(move):
    if max(move) == 0:
        return 0

    if max(move) == 1:
        return 1

    if type(move) is list:
        move = tuple(sorted(move, reverse=True))

    if move in move_dict:
        return move_dict[move]

    # print move
    max_pan = move[0]

    best_ret = max(move)
    rest = list(move[1:])

    for i in range(2, int(math.floor(max_pan / 2)+1)):
        tmp_move = sorted([i, max_pan - i] + rest, reverse=True)
        tmp_ret = solve(tmp_move) + 1

        best_ret = min(tmp_ret, best_ret)

    move_dict[move] = best_ret
    return best_ret


if __name__ == "__main__":
    fp = open("B.in")
    sys.stdout = open("B.out", "w")
    # fp = sys.stdin

    T = int(fp.readline())
    for t in range(T):
        D = int(fp.readline())
        Dz = map(int, fp.readline().split())
        ans = solve(Dz)
        print "Case #%s: %s" % (t + 1, ans)


