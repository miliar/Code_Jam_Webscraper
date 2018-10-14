#! /usr/bin/env python

import sys


def flip(c):
    if c is '-':
        return '+'
    else:
        return '-'


def move(S, K, i):
    prefix = S[:i]
    toflip = S[i:][:K]
    rest = S[i:][K:]
    return prefix + ''.join([flip(c) for c in toflip]) + rest


def solve(S, K):
    if '-' not in S:
        return 0
    if '-' in S and K > len(S):
        return None

    moves = 0
    if S[0] is '-':
        S = move(S, K, 0)
        moves = 1

    n = solve(S[1:], K)
    if n is not None:
        return n + moves
    else:
        return n


if __name__ == '__main__':
    sys.setrecursionlimit(2000)
    with open(sys.argv[1]) as f:
        lines = f.readlines()
    for index, line in enumerate(lines[1:]):
        sys.stdout.write("Case #%s: " % (index + 1))
        S, K = line.strip().split()
        result = solve(S, int(K))
        if result is None:
            print('IMPOSSIBLE')
        else:
            print(result)
        # allmoves = all({S: 0}, int(K))
        # final = '+' * len(S)
        # if final in allmoves:
        #     print(allmoves[final])
        # else:
        #     print('IMPOSSIBLE')
