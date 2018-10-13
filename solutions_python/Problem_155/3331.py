#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def get_next_format_string_index(format_string, current_index):
    if current_index is None or current_index < 0 or current_index >= len(format_string) - 1:
        current_index = 0
    else:
        current_index += 1
    return current_index

# TODO: resolve each test case one by one instead of loading the whole input in one go
def read_input(input_file, input_format_string):
    _ = int(input_file.readline())  # Number of test cases, not returned
    test_cases = []

    fs_index = None
    current_test_case = []
    for line in input_file:
        fs_index = get_next_format_string_index(input_format_string, fs_index)

        # Get rid of potential (leading or trailing) blanks
        line = line.strip()

        if input_format_string[fs_index] == '#':  # We want to ignore this line
            pass
        elif input_format_string[fs_index] == 'I':  # We expect an integer
            current_test_case.append(int(line))
        elif input_format_string[fs_index] == 'S':  # We expect a string
            current_test_case.append(line)
        elif input_format_string[fs_index] == 'L':  # We expect a list of string
            current_test_case.append(line.split())
        elif input_format_string[fs_index] == 'T':  # We expect a list of string
            current_test_case.append([int(s.strip()) for s in line.split()])

        if fs_index >= len(input_format_string) - 1:  # Have we finished getting the test case description?
            test_cases.append(current_test_case)
            current_test_case = []

    return test_cases
    
def write_output(output_file, no_test_case, output_data):
    if no_test_case == None:
        no_test_case = 1
    print('Case #%u: %s' % (no_test_case, ' '.join((str(x) for x in output_data))), file=output_file)
    return no_test_case + 1

def solve_problem(input_data):
    S_max = int(input_data[0][0])
    audience_Si = [int(input_data[0][1][k]) for k in range(len(input_data[0][1]))]
    
    if S_max == 0: return [0]
    
    nb_people_up = audience_Si[0]
    nb_friends = 0
    for j in range(1, len(audience_Si)):
        if nb_people_up + nb_friends < j:
            nb_friends = j - nb_people_up
        nb_people_up += audience_Si[j]
    return [nb_friends]

if __name__ == '__main__':
    import sys

    no_test_case = None
    for test_case in read_input(sys.stdin, 'L'):  # TODO: don't forget to update input_format_string !!!
        no_test_case = write_output(sys.stdout, no_test_case, solve_problem(test_case))
