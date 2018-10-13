#!/usr/bin/python

import sys


def get_min_expected_keys(A, B, prob):
    prob_mul = []
    prod = 1
    for p in prob:
        prod = prod * p
        prob_mul.append(prod)

    mn = None
    for k in range(0, A):
        exp = (2*k + 2*B - A + 2) - prob_mul[A - 1 - k] * (B + 1)
        if mn is None:
            mn = exp
        elif mn > exp:
            mn = exp
    exp2 = B + 2
    if (mn > exp2):
        mn = exp2

    return mn

if __name__ == '__main__':
    T = int(sys.stdin.readline().strip())
    for i in range(1, T+1):
        A, B = tuple([int(k) for k in sys.stdin.readline().strip().split()])
        prob = [float(k) for k in sys.stdin.readline().strip().split()]
        mn = get_min_expected_keys(A, B, prob)
        print "Case #{0}: {1}".format(i, mn)
