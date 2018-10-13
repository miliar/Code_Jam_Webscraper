#!/usr/bin/python3

import re
import math


def calc_surface(pancake):
    return math.pi * pancake[0] ** 2


def calc_margin(pancake):
    return 2.0 * math.pi * pancake[0] * pancake[1]


def sum_stack_margins(num_choose, pancakes):
    items = [(calc_margin(pancake), pancake[0], pancake[1]) for pancake in pancakes]
    items = list(reversed(sorted(items)))
    items = items[:num_choose]
    items = [item[0] for item in items]
    return sum(items)



def solve(N, K, pancakes):
    pancakes = list(reversed(sorted(pancakes)))

    best = 0
    for start_idx in range(N - K + 1):
        battle = calc_surface(pancakes[start_idx]) + \
                calc_margin(pancakes[start_idx]) + \
                sum_stack_margins(K - 1, pancakes[start_idx + 1:])
        best = max(battle, best)

    return best


def main():
    T = int(input())

    for idx in range(T):
        line = input()
        tokens = re.split(' ', line)
        N = int(tokens[0])
        K = int(tokens[1])

        pancakes = []
        for i in range(N):
            line = input()
            tokens = re.split(' ', line)
            Ri = int(tokens[0])
            Hi = int(tokens[1])
            pancakes.append((Ri, Hi))

        result = solve(N, K, pancakes)

        print('Case #{}: {}'.format(idx + 1, '%.6f' % result))

if __name__ == '__main__':
    main()
