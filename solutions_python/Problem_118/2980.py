#!/usr/bin/env python

import sys
from math import ceil

# INPUT
arg = sys.argv[1]
i_file = open(arg, 'r')
nb = int(i_file.readline())
cases = [X.split() for X in i_file.readlines()]
final_list = list()
for [down, up] in cases:
    final_list.append([int(ceil(int(down)**0.5)),
                       int(int(up)**0.5)])

# OUTPUT
o_file = open('output.out', 'w')
global case_nb
case_nb = 0

def is_fair(entier):
    b = str(entier)
    if len(b) == 1:
        return True
    if (b[:len(b)/2] == b[(len(b)+1)/2:][::-1]):
        return True
    else:
        return False

def put_result(entier):
    global case_nb
    
    case_nb += 1
    string = "Case #%s: %s \n" %(str(case_nb), str(entier))
    o_file.write(string)
    # print string


for case in final_list:
    nb_cases = 0
    # print "--------------\ncase %s" %str(case_nb+1)
    for i in range(case[0], case[1]+1):
        if is_fair(i) and is_fair(i**2):
            # print i, i**2, "\n- -"
            nb_cases += 1
    put_result(nb_cases)
