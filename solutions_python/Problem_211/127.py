#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3
# vi: set fileencoding=utf-8 :

import math


def up_base(N, K, U, P):
    base = P[0]
    second = base
    for i in range(N):
        if P[i] > base:
            second = P[i]
            break
    else:
        second = 1
        i += 1
    if i * (second - base) > U:
        for j in range(i):
            P[j] += U / i
        return 0
    else:
        for j in range(i):
            P[j] = second
        return U - i * (second - base)



def solve(N, K, U, P):
    P.sort()
    while U > 10 ** -10:
        U = up_base(N, K, U, P)
    prob = 1
    for i in range(K):
        prob *= P[i]
    return prob


def answer():
    T = int(input())
    for case_number in range(1, T + 1):
        N, K = map(int, input().split())
        U = float(input())
        P = list(map(float, input().split()))
        print('Case #{0}: {1:.6f}'.format(case_number, solve(N, K, U, P)))
    return


if __name__=='__main__':
    import sys
    answer()
