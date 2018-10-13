import fileinput
from time import time


# Solve problem

def add_interval(intervals, interval_size, times):
    if interval_size in intervals:
        intervals[interval_size] += times
    else:
        intervals[interval_size] = times


def remove_interval(intervals, interval_size, times):
    intervals[interval_size] -= times
    if intervals[interval_size] is 0:
        del intervals[interval_size]


def get_biggest_interval(intervals):
    return max(intervals.keys())


def lower_half(number):
    return int(number // 2)


def upper_half(number):
    return number - lower_half(number)


def solve_problem(n, k):
    intervals = dict()
    intervals[n] = 1
    i = 0
    while i < k - 1:
        used_interval = get_biggest_interval(intervals)
        times = intervals[used_interval]
        if i + times >= k - 1:
            times = max(1, times - 1)
        remove_interval(intervals, used_interval, times)
        add_interval(intervals, lower_half(used_interval - 1), times)
        add_interval(intervals, upper_half(used_interval - 1), times)
        i += times

    final_interval = get_biggest_interval(intervals)
    return upper_half(final_interval - 1), lower_half(final_interval - 1)


# Utils


def parse_problem(case):
    [n, k] = case.split(' ')
    return int(n), int(k)


def solve_case(case, case_number):
    n, k = parse_problem(case)
    final_max, final_min = solve_problem(n, k)
    print("Case #" + str(case_number) + ": " + str(final_max) + " " + str(final_min))


# Main script

def main():
    for index, line in enumerate(fileinput.input()):
        if index is 0:
            continue

        line = line.strip()
        solve_case(line, index)

if __name__ == "__main__":
    main()
