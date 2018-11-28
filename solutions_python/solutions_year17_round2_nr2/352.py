"""
Code Jam 2017 / 1B (2017-04-22)
Problem B. Stable Neigh-bors

Author: Ben Feinstein
"""
import numpy as np

IMPOSSIBLE = 'IMPOSSIBLE'
RED = 'R'
YELLOW = 'Y'
BLUE = 'B'


def read_int():
    return int(input())


def read_ints():
    return [int(x) for x in input().split()]


def order_stalls_small(N, R, Y, B):
    colors = sorted([[R, RED], [Y, YELLOW], [B, BLUE]], reverse=True)
    order = [''] * N
    c = 0
    for i in range(0, N, 2):
        while colors[c][0] == 0:
            c = (c + 1) % len(colors)
        order[i] = colors[c][1]
        colors[c][0] -= 1

    for j in range(1, N, 2):
        while colors[c][0] == 0:
            c = (c + 1) % len(colors)
        order[j] = colors[c][1]
        colors[c][0] -= 1

    return ''.join(order)


def order_stalls(N, R, O, Y, G, B, V):
    assert N == R + O + Y + G + B + V, "bad input"
    R_ = R + O + V
    Y_ = Y + O + G
    B_ = B + V + G

    # Pigeonhole principle
    for c in [R_, Y_, B_]:
        if c > N // 2:
            return IMPOSSIBLE

    if O + V + G == 0:
        # small input
        return order_stalls_small(N, R, Y, B)

    else:
        pass


def main():
    T = read_int()
    for test_case in range(1, T + 1):
        N, R, O, Y, G, B, V = read_ints()

        stalls = order_stalls(N, R, O, Y, G, B, V)
        print('Case #%d: %s' % (test_case, stalls))


if __name__ == '__main__':
    main()
