#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3
# vi: set fileencoding=utf-8 :

import math


def busy(C):
    if C[1][1] - C[0][0] <= 1440 / 2:
        return 2
    if C[0][1] + (1440 - C[1][0]) <= 1440 / 2:
        return 2
    return 4


def solve(C, J):
    if len(C) + len(J) <= 1:
        return 2
    C.sort()
    J.sort()
    if len(C) == 2:
        return busy(C)
    if len(J) == 2:
        return busy(J)
    return 2 


def answer():
    T = int(input())
    for case_number in range(1, T + 1):
        A_C, A_J = map(int, input().split())
        C = []
        for a in range(A_C):
            start, end = map(int, input().split())
            C += [(start, end)]
        J = []
        for a in range(A_J):
            start, end = map(int, input().split())
            J += [(start, end)]
        print('Case #{0}: {1}'.format(case_number, solve(C, J)))
    return


if __name__=='__main__':
    import sys
    answer()
