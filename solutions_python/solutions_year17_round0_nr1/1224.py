#!/usr/bin/python3

import re

def solve(S, K):
    S = [pancake == '+' for pancake in S]

    impossible = False
    num_flip = 0
    for idx, pancake in enumerate(S):
        if idx > len(S) - K:
            if not pancake:
                impossible = True
                break
            continue

        if pancake:
            continue

        for jdx in range(idx, idx + K):
            S[jdx] = not S[jdx]

        num_flip += 1

    if impossible:
        return 'IMPOSSIBLE'

    return num_flip


def main():
    T = int(input())

    for idx in range(T):
        line = input()
        tokens = re.split(' ', line)
        S = tokens[0]
        K = int(tokens[1])

        result = solve(S, K)

        print('Case #{}: {}'.format(idx + 1, result))

if __name__ == '__main__':
    main()
