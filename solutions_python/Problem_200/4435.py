# -*- coding: utf-8 -*-
"""
Created on Sat Apr 08 16:15:01 2017

@author: vanisas
"""


def read_input(path_to_file):
    numbers_list = []
    with open(path_to_file) as f:
        for idx, line in enumerate(f):
            if idx == 0:
                testcases = int(line)
            else:
                numbers_list.append(int(line.split(' ')[0]))
    return testcases, numbers_list


def write_output(number_list):
    output_file = open("result-small.out", 'w')
    for idx, line in enumerate(number_list):
        output_file.write('Case #{0}: {1}\n'.format(idx+1, number_list[idx]))
    output_file.close()

def get_tidy_number(number):
    nlist = map(int, list(str(number)))
    prev_list = nlist[:]
    nlist.sort()
    IsSorted = (prev_list == nlist)
    while IsSorted == False:
        number -= 1
        nlist = map(int, list(str(number)))
        prev_list = nlist[:]
        nlist.sort()
        IsSorted = (prev_list == nlist)
    return number
    


if __name__ == "__main__" :
    tidy_list = []
    testcases, numbers_list = read_input("B-small-attempt0.in");
    for i in range(testcases):
        tidy_number = get_tidy_number(numbers_list[i])
        tidy_list.append(tidy_number)
    write_output(tidy_list)
        