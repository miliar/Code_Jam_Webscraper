# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 21:49:32 2017

@author: ntrenchi
"""

def chosen_stall_max_min(number_of_empty_stalls):
    chosen_stall = (number_of_empty_stalls + 1) >> 1
    if number_of_empty_stalls & 1 == 0:
        # even
        chosen_stall_max = chosen_stall
        chosen_stall_min = chosen_stall - 1
    else:
        # odd
        chosen_stall_max = chosen_stall - 1
        chosen_stall_min = chosen_stall - 1
    return chosen_stall, chosen_stall_max, chosen_stall_min


def power_of_two(num):
    # true if num is power of two
    return num & (num - 1)  == 0
#
#def get_last_number_of_empty_stalls(number_of_empty_stalls, incoming_people):
#    remaining_people = incoming_people
#    if incoming_people == 1: return number_of_empty_stalls
#    if number_of_empty_stalls & 1 == 0:
#        # even
#        i = 0
#        last_left = 1
#        last_right = 1
#        while True:
#            i += 1
#            k = 2 ** i
#            
#            # if last number of stalls was not even
#            if number_of_empty_stalls & 1 > 0:
#                last_left = k - last_right
#            last_right = k - last_left
#            
#            # split number of stalls
#            number_of_empty_stalls = number_of_empty_stalls >> 1
#            
#            print(number_of_empty_stalls, last_left, last_right)
#            
#            if remaining_people - last_left <= 1:
#                return number_of_empty_stalls
#            
#            remaining_people -= last_left
#            
#            if remaining_people - last_right <= 1:
#                return number_of_empty_stalls - 1
#            
#            remaining_people -= last_right
#            
#    else:
#        # odd
#        i = 0
#        while True:
#            i += 1
#            k = 2 ** i
#            
#            # split number of stalls
#            number_of_empty_stalls = number_of_empty_stalls >> 1
#            
#            if remaining_people - k <= 1:
#                return number_of_empty_stalls
#            
#            remaining_people -= k
#            
#            

#
## only misses one
#def get_last_number_of_empty_stalls(number_of_empty_stalls, incoming_people):
#    remaining_people = incoming_people
#    if remaining_people == 1: 
#        return number_of_empty_stalls
#    
#    i = 0
#    last_left = 1
#    last_right = 1
#    while True:
#        
#        i += 1
#        k = 2 ** i
#        
#        # if last number of stalls was not even
#        if number_of_empty_stalls & 1 > 0:
#            last_left = k - last_right
#        last_right = k - last_left
#        
#        # split number of stalls
#        number_of_empty_stalls = number_of_empty_stalls >> 1
#        
#        # print(number_of_empty_stalls, last_left, last_right, remaining_people)
#        
#        if remaining_people - last_left <= 1:
#            return number_of_empty_stalls
#        
#        remaining_people -= last_left
#        
#        if remaining_people - last_right <= 1:
#            return number_of_empty_stalls - 1
#        
#        remaining_people -= last_right
#        
#        
def get_last_number_of_empty_stalls(number_of_empty_stalls, incoming_people):
    remaining_people = incoming_people
    if remaining_people == 1: 
        return number_of_empty_stalls
    
    i = 0   
    last_left = 1
    last_right = 0
    while True:
        
        i += 1
        k = 2 ** i
        
        # if last number of stalls was not even
        if number_of_empty_stalls & 1 > 0:
            last_left = k - last_right
        last_right = k - last_left
        
        # split number of stalls
        number_of_empty_stalls = number_of_empty_stalls >> 1
        
        # print(number_of_empty_stalls, last_left, last_right, remaining_people)
        
        if remaining_people - last_left <= 1:
            return number_of_empty_stalls
        
        remaining_people -= last_left
        
        if remaining_people - last_right <= 1:
            return number_of_empty_stalls - 1
        
        remaining_people -= last_right



t = int(input())  # number of test cases
for i in range(1, t + 1):
    number_of_empty_stalls, incoming_people = [int(s) for s in input().split(" ")]
    if number_of_empty_stalls == incoming_people:
        chosen_stall_max, chosen_stall_min = (0, 0)
    else:
        last_number_of_empty_stalls = get_last_number_of_empty_stalls(number_of_empty_stalls, incoming_people)
        chosen_stall_relative, chosen_stall_max, chosen_stall_min = chosen_stall_max_min(last_number_of_empty_stalls)
    print("Case #{}: {} {}".format(i, chosen_stall_max, chosen_stall_min))




