#!/usr/bin/env python

def find_min_time_iter(cost_of_farm, farm_rate, victory_number):
    current_rate = 2
    elapsed_time = 0
    for i in range(10000):
        straight_time = victory_number / current_rate
        purchase_time = cost_of_farm / current_rate
        current_rate += farm_rate

        if straight_time < purchase_time + victory_number/current_rate:
            return elapsed_time + straight_time

        elapsed_time += purchase_time
    
    # It is a good enough approximation at this point
    return straight_time

fptr = open('input.txt')

num_testcases = int(fptr.readline())

for case_num in range(num_testcases):
    arr = fptr.readline().split()
    cost_of_farm = float(arr[0])
    farm_rate = float(arr[1])
    victory_number = float(arr[2])

    #min_time = find_min_time(2.0, cost_of_farm, farm_rate, victory_number, 0) 
    min_time = find_min_time_iter(cost_of_farm, farm_rate, victory_number)

    output_string = 'Case #' + str(case_num + 1) + ': '
    output_string += str(min_time)
    print output_string
