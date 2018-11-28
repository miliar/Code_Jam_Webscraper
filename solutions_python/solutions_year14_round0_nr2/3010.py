#!/usr/bin/env python3

base_rate = 2

def optimize_cookies(farm_cost, farm_rate, goal):
    time = 0.0
    rate = base_rate

    breakeven = farm_cost/farm_rate

    while True:
        to_goal = goal/rate
        to_farm = farm_cost/rate
        if to_goal <= to_farm + breakeven:
            return time + to_goal
        else:
            time += to_farm
            rate += farm_rate

T = int(input())
for i in range(1, T + 1):
    line = input().split(' ')
    C = float(line[0])
    F = float(line[1])
    X = float(line[2])

    print('Case #%d: %f' % (i, optimize_cookies(C, F, X)))
