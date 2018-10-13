#!/usr/bin/env python3
# coding=utf-8

import sys


def solve(farm_cost, farm_rate, objective):
    time = 0.0
    cookie_rate = 2.0
    while objective/cookie_rate > (farm_cost/cookie_rate + objective/(cookie_rate+farm_rate)):
        time += farm_cost/cookie_rate
        cookie_rate += farm_rate
        #print('time: {}, rate: {}'.format(time, cookie_rate))
    time += objective/cookie_rate
    return time


def main():
    with open(sys.argv[1]) as f:
        f.readline()
        for i, line in enumerate(f):
            farm_cost, farm_rate, objective = (float(x) for x in line.strip().split())
            res = solve(farm_cost, farm_rate, objective)
            print('Case #{}: {:.7f}'.format(i+1, res))

if __name__ == '__main__':
    main()
