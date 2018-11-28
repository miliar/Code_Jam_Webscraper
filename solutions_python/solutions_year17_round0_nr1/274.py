# coding: utf-8


def solve():
    S, K = input().split()
    S = list(S)
    K = int(K)
    res = 0
    for i in range(len(S) - K + 1):
        if S[i] == '+':
            continue
        for j in range(i, i + K):
            S[j] = '+' if S[j] == '-' else '-'
        res += 1

    if S == list('+' * len(S)):
        return res
    return 'IMPOSSIBLE'

T = int(input())
for tc in range(T):
    res = solve()
    print('Case #{}: {}'.format(tc + 1, res))
