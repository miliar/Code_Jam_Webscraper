#!/usr/bin/python3

import re

def solve(D, N, K, S):
    max_seconds = 0
    for i in range(N):
        battle = (D - K[i]) / S[i]
        max_seconds = max(battle, max_seconds)
    return D / max_seconds

def main():
    T = int(input())

    for idx in range(T):
        line = input()
        tokens = re.split(' ', line)
        D = int(tokens[0])
        N = int(tokens[1])

        K = []
        S = []
        for i in range(N):
            line = input()
            tokens = re.split(' ', line)
            K.append(int(tokens[0]))
            S.append(int(tokens[1]))

        result = solve(D, N, K, S)

        print('Case #{}: {}'.format(idx + 1, '%.6f' % result))

if __name__ == '__main__':
    main()
