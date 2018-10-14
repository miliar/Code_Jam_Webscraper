#!/usr/bin/env python3
import math
inf = float('inf')
read_ints = lambda : list(map(int, input().split()))

def check(N, S):
    for i in range(N):
        if (S[i] != '-') and (S[i] == S[(i+1) % N]):
            return False
    return True

def rec(N, S, left):
    nc, c = left.pop(0)   # next color
    if left == []:
        for i in range(N):
            if (S[i] == '-'):
                S[i] = c
        if check(N, S):
            return S
        return 'IMPOSSIBLE'

    i = 0
    Ncolor = nc
    while Ncolor > 0:
        if S[i] != '-':
            i = (i + 1) % N
        else:
            S[i] = c
            Ncolor -= 1
            i = (i + 3) % N

    while not check (N, S):
        # print("S=", S)
        for i in range (N):
            if S[i] == c and S[(i+1) % N] == c:
                S[(i+1) % N] = '-'
                j = (i+2) % N
                while S[j] != '-':
                    j = (j + 1) % N
                S[j] = c
            i = (i + 1) % N

    # print("S=", S)
    return rec(N, S, left)


def solve(N, R, O, Y, G, B, V):
    left = [(R, 'R'), (Y, 'Y'), (B, 'B')]
    for nc, c in left:
        if nc > math.floor(N / 2):
            return 'IMPOSSIBLE'
    left.sort(reverse=True)

    return rec(N, ['-'] * N, left)

if __name__ == '__main__':
    T = int(input())
    for t in range(1, T+1):
        N, R, O, Y, G, B, V = read_ints()
        print('Case #%d: %s' % (t, ''.join(solve(N, R, O, Y, G, B, V))))
