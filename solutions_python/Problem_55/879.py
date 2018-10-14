

import sys
import os

def print_output(final_solution_list):
    for index, item in enumerate(final_solution_list):
        print 'Case #%s: %s' %(index+1, item) 


def solution_per_case(input_line_1, input_line_2):

    line1 = input_line_1.split(" ")

    r = int(line1[0])
    k = int(line1[1])
    n = int(line1[2])    
     
    line2 = input_line_2.split(" ")  
   
    queue = []
    queue_total = 0
   
    for guest in line2:
        queue.append(int(guest))
        queue_total += int(guest)
 
    r_index = 0
    k_index = 0
    n_index = 0
  
    q_index = 0 
    per_day_revenue = 0  

    while r_index < r:
        people_in_this_round = 0
        start_q_index = q_index
        while (people_in_this_round + queue[q_index]) <= k and (people_in_this_round + queue[q_index]) <= queue_total:
            people_in_this_round += queue[q_index]
            if q_index < (n-1):
                q_index += 1
            elif start_q_index:
                q_index = 0 
            else:
                break
        per_day_revenue += people_in_this_round
        r_index += 1

    return per_day_revenue
        

def process_solution(number_test_cases, input_list_1, input_list_2):
    
    test_case = 0
    number_test_cases = int(number_test_cases)
    final_solution_list = []
 
    while test_case < number_test_cases:
        try:
            input1 = input_list_1[test_case]
            input2 = input_list_2[test_case]
            final_solution_list.append(solution_per_case(input1, input2))
            test_case += 1
        except IndexError:
            print 'exception test_case: %s' %test_case
            
    print_output(final_solution_list)    

def fetch_input(filename):
    try:
        coaster_handle = open(filename, "r") 
    except IndexError:
        logging.debug("file not present")
        return

    input_list_1 = []
    input_list_2 = []
  
    coaster_text = coaster_handle.readlines()
    line_number = 0    
 
    for line in coaster_text:
        if line_number:
            if line_number%2:  # odd case
                input_list_1.append(line)
            else: # even case
                input_list_2.append(line)
            line_number += 1  
        else:
            number_test_cases = line
            line_number += 1


    if len(input_list_1) == len(input_list_2):
        process_solution(number_test_cases, input_list_1, input_list_2)

if __name__ == "__main__":
    filename = sys.argv[1]
    fetch_input(filename)
