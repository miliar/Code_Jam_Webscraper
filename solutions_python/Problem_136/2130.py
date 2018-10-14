#!/usr/bin/env python
# -*- coding: utf-8 -*-

def calculate(data):
    farm_cost = data[0]
    farm_gain = data[1]
    goal = data[2]
    cps = 2.0
    time = 0.0
    while True:
        time_to_farm = time_to(cps, farm_cost)
        time_to_goal = time_to(cps, goal)
        farm_then_goal = time_to_farm + time_to(cps + farm_gain, goal)
        if farm_then_goal < time_to_goal:
            time += time_to_farm
            cps += farm_gain
        else:
            return time + time_to_goal

def time_to(cps, goal):
    return goal / cps

def main():
    input_file = open('B-large-0.in')
    output_file = open('B-large-0.out', 'w')
    cases = int(input_file.readline())
    for case in range(1, cases + 1):
        data = [float(n) for n in input_file.readline().split()]
        solution = calculate(data)
        print(round(solution,7))
	output_file.write('Case #{0}: {1}\n'.format(case, round(solution, 7)))
    input_file.close()
    output_file.close()

if __name__ == '__main__':
    main()
