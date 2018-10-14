#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 00:08:19 2017

@author: asiri
"""
import math


                
def find_longest_index(list_):
    longest = 0
    for i in range(0,len(list_)):
        if len(list_[longest]) < len(list_[i]):
            longest = i
    return longest

def assign_user(list_):
    midpoint = math.floor( (len(list_)+1)/2)
    list_  = list(list_)
    list_[midpoint-1] = '1'
    return ''.join(list_)

def get_min_max(str_):
    l_  = list(str_)
    leading_ = 0
    for i in range(0,len(l_)):
        if l_[i]!='1':
            leading_+=1
        else:
            break
    trailing_ = 0
    for i in range(len(l_)-1,-1,-1):
        if l_[i]!='1':
            trailing_+=1
        else:
            break
    return max([trailing_,leading_]),min([trailing_,leading_])

def calc_stalls(stalls__,users__):

    stalls = stalls__
    total_stalls = stalls + 2
    users = users__
    
    current_bathroom = [0 for x in range(0,total_stalls)]
    current_bathroom[0] = 1
    current_bathroom[-1] = 1
                    
    current_bathroom = ''.join([str(x) for x in current_bathroom])
    
    for n in range(0,users):
        if n!=users-1 :#i.e. not the last one
            comp = current_bathroom.split('1')
            longest_ = find_longest_index(comp)
            assigned_ = assign_user(comp[longest_])
            comp[longest_] = assigned_
            current_bathroom = '1'.join(comp)
        else:
            comp = current_bathroom.split('1')
            longest_ = find_longest_index(comp)
            assigned_ = assign_user(comp[longest_])
            comp[longest_] = assigned_
            current_bathroom = '1'.join(comp)
            a_ = (get_min_max(comp[longest_]))
            return a_
        
        
        

input_lines = open("C-small-1-attempt0.in").readlines()
input_lines = [(x.replace("\n","")) for x in input_lines]

test_cases = input_lines[1:]

out_ = open("quali_smallC.out","w")
for case_ in range(0,len(test_cases)):
    input_ = test_cases[case_].split(" ")
    result_ = calc_stalls(int(input_[0]),int(input_[1]))

    print(case_)
    out_.write("Case #{}: {} {}\n".format(case_+1,result_[0],result_[1]))
out_.close()   







