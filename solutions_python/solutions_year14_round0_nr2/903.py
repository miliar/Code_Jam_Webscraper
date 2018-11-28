#!/usr/bin/env python

import sys

DEFAULT_COOKIE = float(2.0)

def calculate_times(cookie_goal, cost_of_farm, current_harvest_speed, farm_boost, previous_time):
    time_to_goal = previous_time + (cookie_goal / current_harvest_speed)
    time_to_farm = cost_of_farm / current_harvest_speed

    time_to_goal_with_additional_farm = previous_time + time_to_farm + (cookie_goal / (current_harvest_speed + farm_boost))

    return time_to_goal, time_to_goal_with_additional_farm, current_harvest_speed + farm_boost, time_to_farm


def solve_case(case_num):
    nums = [x.strip() for x in sys.stdin.readline().split(' ')]

    cost_of_farm = float(nums[0])
    farm_boost = float(nums[1])
    cookie_goal = float(nums[2])

    time_to_goal, time_to_goal_with_additional_farm, new_harvest_speed,previous_time = calculate_times(
            cookie_goal,
            cost_of_farm,
            DEFAULT_COOKIE,
            farm_boost,
            0
            )

    while time_to_goal_with_additional_farm < time_to_goal:
        time_to_goal, time_to_goal_with_additional_farm, new_harvest_speed, another_farm_time = calculate_times(
            cookie_goal,
            cost_of_farm,
            new_harvest_speed,
            farm_boost,
            previous_time
            )
        previous_time += another_farm_time

    print "Case #%s: %s" % (case_num, time_to_goal)


def main():
    test_cases = sys.stdin.readline()
    cases_solved = 0

    while cases_solved < test_cases:
        cases_solved += 1
        solve_case(cases_solved)

if __name__ == '__main__':
    main()
