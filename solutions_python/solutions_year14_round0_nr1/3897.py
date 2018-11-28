# -*- coding: utf-8 -*-
"""
Created on Sat Apr 12 12:32:33 2014

@author: Euphorbium

Solves google code jam problem 1
"""
import sys
print sys.argv[1]
input_data = open(sys.argv[1], "r").read().splitlines()[::-1]
output_file = open("output.txt", "w")

cases = int(input_data.pop())
for k,j in enumerate(range(cases)):
    first_guess = input_data.pop()
    first_line = input_data[-int(first_guess)].split()
    print first_line
    for i in range(4):
        input_data.pop()
    second_guess = input_data.pop()
    second_line = input_data[-int(second_guess)].split()
    print second_line
    for i in range(4):
        input_data.pop()
    k+=1
    state = len(list(set(first_line).intersection(second_line)))   
    if  state == 1:
        print >> output_file, "Case #%d:" % k, list(list(set(first_line).intersection(second_line)))[0]
    elif state > 1:
        print >> output_file, "Case #%d:" % k, "Bad magician!"
    else:
        print >> output_file, "Case #%d:" % k, "Volunteer cheated!"
        
output_file.close()