#! /usr/bin/env python3

import sys
import typing


def solve(pancakes: typing.List[str], k: int) -> int:
    flips = 0
    flipper = int('1' * k, 2)

    for i in range(len(pancakes)):

        if happy(pancakes[i]):
            continue

        if i + k > len(pancakes):
            return -1

        pancakes[i:i+k] = flip(pancakes[i:i+k], flipper)
        flips += 1

    return flips


def happy(pancake: str) -> bool:
    return pancake == '1'


def flip(buf: typing.List[str], flipper: int) -> str:
    return bin(int(''.join(buf), 2) ^ flipper)[2:]


def main():
    f = open(sys.argv[1], 'r')

    for i, line in enumerate(f):

        if i == 0:
            continue

        parts = line.split(' ')
        pancakes = parts[0].replace('-', '0').replace('+', '1').strip()
        k = int(parts[1])
        flips = solve(list(pancakes), k)
        print('Case #{}: {}'.format(i, flips if flips != -1 else 'IMPOSSIBLE'))
        # print(line.strip())

if __name__ == '__main__':
    main()
