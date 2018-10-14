#! /usr/bin/env python

import sys

INITIAL_RATE = 2

def _estimate_time_direct(C, F, X, rate):
    return X/rate

def _estimate_time_with_farm(C, F, X, rate):
    time_for_farm = C/rate
    new_rate = rate + F
    time_to_win = X/new_rate
    return time_for_farm + time_to_win

def solve_problem(input_file, output_file):
    input_file = open(input_file, 'r')
    output_file = open(output_file, 'w+')
    test_cases = int(input_file.readline())
    for i in range(0, test_cases):
        parameters = input_file.readline().split()
        C = float(parameters[0])
        F = float(parameters[1])
        X = float(parameters[2])
        rate = INITIAL_RATE
        wait_for_farm = True
        total_seconds = 0.0

        while (wait_for_farm):
            time_direct = _estimate_time_direct(C, F, X, rate)
            time_with_farm = _estimate_time_with_farm(C, F, X, rate)

            if time_direct <= time_with_farm :
                wait_for_farm = False
                total_seconds += time_direct
            else:
                total_seconds += C/rate
                rate += F
        line_result = 'Case #{}: {:0.7f}\n'.format(i+1, total_seconds)
        output_file.write(line_result)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        raise Exception('Missing intput/output files')
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    solve_problem(input_file, output_file)

