#!/usr/bin/env python3

def solve(row, K):
    row = [1 if c == '+' else 0 for c in row]
    count = 0

    for i in range(len(row) - (K - 1)):
        if row[i] == 0:
            for j in range(K):
                row[i + j] ^= 1
            count += 1

    solved = True
    for i in range(len(row) - (K - 1), len(row)):
        if row[i] == 0:
            return 'IMPOSSIBLE'

    return str(count)


T = int(input())
for t in range(T):
    a, b = input().split()
    res = solve(a, int(b))
    print('Case #{}: {}'.format(t+1, res))

