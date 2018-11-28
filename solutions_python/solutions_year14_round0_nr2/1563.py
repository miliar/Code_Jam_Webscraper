#!/usr/bin/python

import collections

def solution(case, text):
    with open("output.txt", "a") as output_file:
        output_file.write("Case #{0}: {1}\n".format(case, text))

def next_step(c, f, x, rate, cookies):
    seconds = (c - cookies) / rate
    cookies = 0
    rate = rate + f
    aux = x / rate
    seconds = seconds + (x / rate)
    return seconds

def solve_problem(case, c, f, x):
    cookies = 0
    rate = 2.0
    total_seconds = 0.0
    possible_seconds = 0.0
    final_seconds = 1.0
    
    while( possible_seconds < final_seconds ):
        seconds = (c - cookies) / rate
        final_seconds = x / rate
        possible_seconds = next_step(c, f, x, rate, cookies)
        
        if final_seconds <= possible_seconds:
            total_seconds = total_seconds +  final_seconds
        else:
            total_seconds = total_seconds + seconds
            cookies = 0
            rate = rate + f
            
    res = "%.7f" % total_seconds
    solution(case, str(res))
        
with(open("input.txt", "r")) as input_file:
    test_cases = input_file.readline()
    
    for i in range(1, int(test_cases) + 1):
        line = input_file.readline()
        line = line[:-1]
        numbers = line.split(' ')
        solve_problem(i, float(numbers[0]), float(numbers[1]), float(numbers[2]))










