#!/usr/bin/env python3

inf = float('inf')
read_ints = lambda : list(map(int, input().split()))

def flip(S, i):
    if S[i] == '+':
        S[i] = '-'
    else:
        S[i] = '+'

def solve(S, K):
    ans = 0
    for i in range(len(S)):
        if S[i] == '-':
            ans += 1
            if i + K - 1 < len(S):
                for j in range(K):
                    flip(S, i + j)
    if S == ['+'] * len(S):
        return str(ans)
    return 'IMPOSSIBLE'

if __name__ == '__main__':
    T = int(input())
    for t in range(1, T+1):
        S, K = input().split()
        K = int(K)
        S = list(S)
        print('Case #%d: %s' % (t, solve(S, K)))
