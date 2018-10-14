#! /usr/bin/env python3


def calculate_speed(destination, n, horses):
    minimum_time = 0
    for start, speed in horses:
        horse_time = (destination - int(start)) / int(speed)
        minimum_time = max(minimum_time, horse_time)
    return destination / minimum_time


if __name__ == '__main__':
    t = int(input())
    for case in range(t):
        d, n = [int(ele) for ele in input().split()]
        horses = [input().split() for _ in range(n)]
        print("Case #{}: {}".format(case + 1, calculate_speed(d, n, horses)))
