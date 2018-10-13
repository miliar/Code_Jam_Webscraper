# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 18:38:18 2017

@author: lucep_000
"""
def solve_problem(string_n):
    list_number = [int(float(k)) for k in string_n]
    len_n = len(string_n)
    index_even_cur = 0
    index_first_failed = len_n
    for i in range(0, len_n-1):
        if list_number[i]<list_number[i+1]:
            index_even_cur = i+1
        elif list_number[i]==list_number[i+1]:
            continue
        else:
            index_first_failed = i+1
            break
    if index_first_failed == len_n:
        list_solved = list_number
    else:
        list_solved = list_number[0:index_even_cur]+ [list_number[index_even_cur]-1]+ [9] * (len_n-index_even_cur-1)
    list_string = ''.join(map(str, list_solved))
    return int(list_string)
                  

import sys
file_in = sys.argv[1]
file_out = sys.argv[2]
with open(file_in, "r+") as f:
    #f.seek(0)
    # input() reads a string with a line of input, stripping the '\n' (newline) at the end.
    # This is all you need for most Google Code Jam problems.
    with open(file_out, "w+") as outfile:
        t = int(f.readline())  # read a line with a single integer
        for i in range(1, t + 1):
            string_n = str(f.readline().replace('\n', '').strip())
            result = solve_problem(string_n)
            outfile.write("Case #{}: {}".format(i, result) +'\n')
            print("Case #{}: {}".format(i, result))
            # check out .format's specification for more formatting options