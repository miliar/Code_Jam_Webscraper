#!/usr/bin/env python3

T = int(input())

def split(P, d, m):
    P = list(P)
    for i in range(len(P)):
        if P[i] == m:
            P[i] = m // d
            P.append(m - P[i])
            break
    return P


def optimize(P, i, best):
    m = max(P)
    if m <= 2:
        return min(best, i + m)

    if i >= best:
        return best

    Pm1 = [p - 1 for p in P]
    best = optimize(Pm1, i + 1, best)

    for d in range(2, (m // 2) + 1):
        best = optimize(split(P, d, m), i + 1, best)

    return best


for n in range(T):
    D = int(input())
    P = [int(p) for p in input().split()]
    print('Case #{0}: {1}'.format(n + 1, optimize(P, 0, max(P))))
