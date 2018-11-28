#!/usr/bin/env python3
from math import ceil

def growth_rate(nfarms, farm_output):
    return float((nfarms * farm_output) + 2)

def time_to_target(growth_rate, target):
    return float(target) / float(growth_rate)

def time_to_next_farm(growth_rate, farm_cost):
    return time_to_target(growth_rate, farm_cost)

def do_case(caseid):
    farm_cost, farm_output, target = tuple(map(float, input().split()))
    target_farms = max(ceil((target / farm_cost) - (2.0 / farm_output) - 1), 0)
    time = 0.0
    for i in range(target_farms):
        time += time_to_next_farm(growth_rate(i, farm_output), farm_cost)
    time += time_to_target(growth_rate(target_farms, farm_output), target)
    print('Case #{0}: {1:.7f}'.format(caseid, time))

def main():
    num_inputs = int(input())
    for k in range(num_inputs):
        do_case(k + 1)

if __name__ == '__main__':
    main()
