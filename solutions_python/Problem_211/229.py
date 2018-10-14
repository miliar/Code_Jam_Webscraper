#!/usr/bin/env python3

from operator import mul
from functools import reduce


def next_target(cores, index):
    try:
        return cores[index+1]
    except IndexError:
        return 1.0


def train(power, cores):
    index = 0
    cores.sort()
    while round(power, 6) > 0:
        target = next_target(cores, index)
        margin = target - cores[index]
        index += 1
        training_power = margin * index
        if training_power <= power:
            cores[:index] = [target] * index
            power -= training_power
        else:
            cores[:index] = [core + power/index for core in cores[:index]]
            power = 0
        if all(round(core, 6) == 1.0 for core in cores):
            break
    return reduce(mul, cores)


def main():
    for case in range(int(input())):
        _ = [int(n) for n in input().split()]
        power = float(input())
        cores = [float(n) for n in input().split()]
        answer = train(power, cores)
        print('Case #{}: {}'.format(case+1, answer))


if __name__ == '__main__':
    main()
