#!/usr/bin/env python
# -*- coding: utf-8 -*-

def open_file(file_name):
    with open(file_name) as f:
        line_cnt = int(f.readline())
        case_list = []
        for i in range(0, line_cnt):
            case_list.append(int(f.readline()))
        return case_list

def find_last_fidy_number(str_n):
    if len(str_n) == 1:
        return str_n

    d_list = [int(d) for d in str_n]
    index = -1
    for i in range(0, len(d_list) - 1):
        if d_list[i] > d_list[i + 1]:
            index = i
            break
    if index == -1:
        return str_n

    d_head = d_list[0: index + 1]
    str_head = ""
    for i in d_head:
        if i is not 0:
            str_head += str(i)
    str_head = str(int(str_head) - 1)
    if str_head == "0":
        str_head = ""

    tidy_head = find_last_fidy_number(str_head)
    tidy_tail = "9" * (len(d_list) - index - 1)
    return tidy_head + tidy_tail

def solve_one_case(case):
    return find_last_fidy_number(str(case))

def solve_all(case_list, out_file):
    with open(out_file, 'w') as f:
        for i, case in enumerate(case_list):
            res = solve_one_case(case)
            """
            Case #1: 129
            Case #2: 999
            Case #3: 7
            Case #4: 99999999999999999
            """
            line = "Case #" + str(i + 1) + ": " + str(res)
            f.write(line)
            f.write("\n")

if __name__ == "__main__":
    #case_list = open_file("test_case")
    #solve_all(case_list, "test_case_out")
    #case_list = open_file("B-small-attempt0.in")
    #solve_all(case_list, "B-small-attempt0.out")
    case_list = open_file("B-large.in")
    solve_all(case_list, "B-large.out")


