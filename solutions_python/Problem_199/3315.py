#!/usr/bin/env python3

import os
import sys


def flip_pancakes(inp, pos, size):
    for i in range(pos, pos + size):
        if inp[i] == '-':
            inp = inp[:i] + '+' + inp[i + 1:]
        else:
            inp = inp[:i] + '-' + inp[i + 1:]

    return inp


def main():
    T = int(input())
    for i in range(T):
        line = input()
        S, K = line.split()
        K = int(K)
        num_flips = 0

        for idx in range(len(S)):

            if (len(S) - idx < K) and ('-' in S[idx:]):
                num_flips = 'IMPOSSIBLE'
                break
            if S[idx] == '-':
                S = flip_pancakes(S, idx, K)
                num_flips += 1

        print('Case #{}: {}'.format(i + 1, num_flips))


if __name__ == '__main__':
    main()
