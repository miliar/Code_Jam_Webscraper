"""
Code Jam 2017 / 1B (2017-04-22)
Problem A. Steed 2: Cruise Control

Author: Ben Feinstein
"""
import numpy as np


def read_int():
    return int(input())


def read_ints():
    return [int(x) for x in input().split()]


def max_velocity(D, K, S):
    # remove illegal values
    idxs = (0 <= K) & (K < D)
    K = K[idxs]
    S = S[idxs]
    T = (D - K) / S

    return D / np.max(T)


def main():
    T = read_int()
    for test_case in range(1, T + 1):
        D, N = read_ints()
        K = np.zeros(N, dtype=np.float)
        S = np.zeros(N, dtype=np.float)
        for i in range(N):
            K[i], S[i] = read_ints()

        velocity = max_velocity(D, K, S)
        # noinspection PyStringFormat
        print('Case #%d: %.6f' % (test_case, velocity))


if __name__ == '__main__':
    main()
