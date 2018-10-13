#!/usr/bin/env python3


import sys
from numpy import *
from functools import reduce
import operator
import numpy as np
input_file = open(sys.argv[1], 'r')
output_file = open("out_" + sys.argv[0].rstrip("."), 'w')

input_size = int(input_file.readline().rstrip("\n"))



def cut_line(line, s):
    for i in range(len(line)):
        if line[i] > s:
            line[i] = s
    return line

def is_line_doable(line, size):
    return len([i for i in line if i > size]) == 0

case = 1 
for i in range(input_size):
    global values
    values = []
    global N,M
    
    (N, M) = map(int, input_file.readline().rstrip("\n").split(" "))
    # N = nombre de lignes
    # M = nombre de colonnes
    global input_field
    input_field = np.zeros((N,M))
    output_field = np.zeros((N,M))
    output_field.fill(101)
    for i in range(N):
        input_field[i] = input_file.readline().rstrip("\n").split(" ")
    values = sorted(list(reduce(operator.or_, map(set, input_field))))
    for value in values:
        for i in range(N):
            for j in range(M):
                if(input_field[i,j] == value):
                    if(is_line_doable(input_field[:,j], value)):
                        output_field[:,j] = cut_line(output_field[:,j], value)
                    elif (is_line_doable(input_field[i][:], value)):
                        output_field[i,:] = cut_line(output_field[i,:], value)
    if((input_field == output_field).all()):
        output_file.write("Case #"  + str(case) + ": YES\n")
        case += 1
    else:
        output_file.write("Case #"  + str(case) + ": NO\n")
        case += 1
    
                                                 
                
