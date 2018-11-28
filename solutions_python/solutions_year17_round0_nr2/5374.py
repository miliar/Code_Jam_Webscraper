# Problem B. Tidy Numbers
# Problem

# Tatiana likes to keep things tidy. Her toys are sorted from smallest to largest, her pencils are sorted from shortest to longest and her computers from oldest to newest. One day, when practicing her counting skills, she noticed that some integers, when written in base 10 with no leading zeroes, have their digits sorted in non-decreasing order. Some examples of this are 8, 123, 555, and 224488. She decided to call these numbers tidy. Numbers that do not have this property, like 20, 321, 495 and 999990, are not tidy.
#
# She just finished counting all positive integers in ascending order from 1 to N. What was the last tidy number she counted?
#
# Input
#
# The first line of the input gives the number of test cases, T. T lines follow. Each line describes a test case with a single integer N, the last number counted by Tatiana.
#
# Output
#
# For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the last tidy number counted by Tatiana.
#
# Limits
#
# 1 ≤ T ≤ 100.
# Small dataset
#
# 1 ≤ N ≤ 1000.
# Large dataset
#
# 1 ≤ N ≤ 1018.
# Sample
#
#
# Input
#
# Output
#
# 4
# 132
# 1000
# 7
# 111111111111111110
#
# Case #1: 129
# Case #2: 999
# Case #3: 7
# Case #4: 99999999999999999
#
# Note that the last sample case would not appear in the Small dataset.

import hashlib


def process_inputs(file_prefix):
    with open(file_prefix + '.in', 'r') as f:
        # first line is T
        t = int(f.readline())
        for i in range(t):
            print('processing case {i}'.format(i=i + 1))
            yield process_single_case(f)


def process_single_case(f):
    """
    :param f: input file descriptor  
    :return: case processed 
    """
    last_number = str(int(f.readline()))
    while not check_sorted_number(last_number):
        last_number = next_sorted(last_number)
    return int(last_number)


def next_sorted(original_n):
    """asuming it is not sorted, check from right to left while n and p is >= when not return the next n(p-1)9999..."""
    str_n = '0' + original_n
    i_n, i_p = -2, -1
    while not str_n[i_n] < str_n[i_p]:
        i_n, i_p = i_n - 1, i_p - 1
    upper_str = str_n[:i_n + 1] + str(int(str_n[i_p]) - 1)
    needed_n = len(original_n) + 1 - len(upper_str)
    rest_nines = '9' * abs(needed_n)
    return upper_str + rest_nines


def check_sorted_number(str_n):
    if len(str_n) == 1:
        return True
    last = str_n[0]
    for n in str_n[1:]:
        if n < last:
            return False
        last = n
    return True


def write_output(processed_cases, file_prefix):
    with open(file_prefix + '.out', 'w') as f:
        for i, case_result in enumerate(processed_cases):
            i_case = i + 1
            print('{}: {}'.format(i_case, case_result))
            write_single_result(f, i_case, case_result)
    f.close()


def write_single_result(f, i, case_result):
    """
    writes on the output file the results of the i case formatted
    :param f: output file descriptor 
    :param i: index number the processed case
    :param case_result: case result
    """
    f.write('Case #{i}: {case_result}\n'.format(**locals()))


def cmp_files(file_name1, file_name2):
    with open(file_name1) as f1, open(file_name2) as f2:
        for line1, line2 in zip(f1, f2):
            l1, l2 = line1.strip(), line2.strip()
            if l1 != l2:
                print('Fail! {} =! {}'.format(l1, l2))
                return False
    return True


if __name__ == '__main__':
    # file_prefix = 'B-small-attempt3'
    file_prefix = 'B-small-attempt4'
    check_tests = False
    if check_tests:
        file_prefix += '-test'
        write_output(process_inputs(file_prefix), file_prefix)
        assert cmp_files(file_prefix + '.out', file_prefix + '-check.out') is True
    else:
        write_output(process_inputs(file_prefix), file_prefix)
