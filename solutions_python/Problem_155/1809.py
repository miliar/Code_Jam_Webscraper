#!/usr/bin/python

import sys

def convert_input(input_string):
    pair = input_string.split()
    Smax = int(pair[0])
    digit_str = pair[1]
    digit_list = []
    no_zero = True

    for idx in xrange(len(digit_str)):
        curr_char = digit_str[idx]
        digit_list.append(int(curr_char))
        if curr_char == '0':
            no_zero = False

    if no_zero:
        Smax = 0

    return [Smax, digit_list]

def invitation_number(Smax, digit_list):
    already_have = 0
    still_need = 0

    for idx in xrange(len(digit_list)):
        if digit_list[idx] != 0:
            if still_need + already_have < idx:
                still_need = idx - already_have
            already_have += digit_list[idx]

    return still_need

def run():

    in_name = str(sys.argv[1])
    fo_in = open(in_name, "r")

    first_line = fo_in.readline()
    test_cases = int(first_line)

    for idx in xrange(test_cases):
        curr_line = fo_in.readline()
        res_list = convert_input(curr_line)
        curr_case = str(idx + 1)
        if res_list[0] == 0:
            print "Case #" + curr_case + ": 0"
        else:
            res = invitation_number(res_list[0], res_list[1])
            print "Case #" + curr_case + ": " + str(res)

    fo_in.close()

run()
