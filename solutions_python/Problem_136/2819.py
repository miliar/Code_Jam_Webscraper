#!/usr/bin/env python3

import sys

def calc_naive(time_elapsed, goal, cookie_rate):
    return time_elapsed + (goal / cookie_rate)

def calc_factory(time_elapsed, cost, cookie_rate, goal, production):
    next_factory_time = calc_next_factory(time_elapsed, cost, cookie_rate)
    return next_factory_time + (goal / (cookie_rate + production))

def calc_next_factory(time_elapsed, cost, cookie_rate):
    return time_elapsed + (cost / cookie_rate)

def play_game(cookie_rate, time_elapsed, cost, production, goal):
    naive_time = calc_naive(time_elapsed, goal, cookie_rate)
    factory_win_time = calc_factory(time_elapsed, cost, cookie_rate, goal, production)

    while (factory_win_time < naive_time):
        time_elapsed = calc_next_factory(time_elapsed, cost, cookie_rate)
        cookie_rate += production
        naive_time = calc_naive(time_elapsed, goal, cookie_rate)
        factory_win_time = calc_factory(time_elapsed, cost, cookie_rate, goal, production)

    return naive_time

input = open(sys.argv[1], "r")
output = open("output.out", "w")

test_cases = int(input.readline())

for case in range(0, test_cases):
    data = input.readline().split()
    cost = float(data[0])
    production = float(data[1])
    goal = float(data[2])
    cookie_rate = 2.0
    time_elapsed = 0.0
    time_to_win = play_game(cookie_rate, time_elapsed, cost, production, goal)
    output_string = "Case #{0}: {1:.7f}\n".format(case + 1, time_to_win)
    output.write(output_string)

input.close()
output.close()
