# coding: utf-8

from fractions import Fraction
import functools
import operator


def array2d(d1, d2, init=None):
    return [[init for _ in range(d2)] for _ in range(d1)]


def solve():
    N, K = map(int, input().split(" "))
    U = Fraction(input())
    Cores = list(map(Fraction, input().split(" ")))

    # small
    if N != K:
        return 0.0
    Cores.sort()
    while U > 0:
        # print(list(map(float, Cores)))
        min_core_cnt = 1
        for i in range(1, N):
            if Cores[i] == Cores[0]:
                min_core_cnt += 1
            else:
                break
        if min_core_cnt == N:
            Cores = [c + U/N for c in Cores]
            U = 0
        else:
            d = Cores[min_core_cnt] - Cores[0]
            if d * min_core_cnt <= U:
                for i in range(0, min_core_cnt):
                    Cores[i] += d
                U -= d * min_core_cnt
            else:
                for i in range(0, min_core_cnt):
                    Cores[i] += U/min_core_cnt
                U = 0

    return float(functools.reduce(operator.mul, Cores))


def main():
    n_cases = int(input())
    for i in range(n_cases):
        print("Case #{}: {}".format(i + 1, solve()))


if __name__ == "__main__":
    main()
