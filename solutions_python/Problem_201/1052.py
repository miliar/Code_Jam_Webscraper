# -*- coding: utf-8 -*-

import math


def get_level(K):  # do not use math module to avoid non-integer operation
    level = 0
    powered = 1
    while True:
        powered *= 2
        if powered > K:
            return level
        level += 1


def get_stall_seq_size(N, K):
    level = get_level(K)

    p = N - (2 ** level - 1)
    q = min(p, 2 ** level)

    if p % q == 0:
        return p / q
    else:
        a = int(math.floor(p / q))
        b = int(math.ceil(p / q))
        if K <= N - a * q:
            return b
        else:
            return a


def f(N, K):
    S = get_stall_seq_size(N, K)  ## size of the sequence of stalls, which the Kth person will enter
    if S % 2 == 0:
        return (S / 2, S / 2 - 1)
    else:
        return ((S - 1) / 2, (S - 1) / 2)


def main():
    T = int(input())
    for i in range(T):
        x = i + 1

        N, K = map(int, input().split())
        y, z = f(N, K)

        print("Case #%d: %d %d" % (x, y, z))


if __name__ == '__main__':
    main()
