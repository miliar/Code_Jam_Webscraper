# GCJ 2013 Qualification Round
# Fair and Square
# A fair number is an integer palindrome, i.e. 121, 676, etc. which
# reads the same forward and backward. A 'fair and square' number is
# one that is fair as well as being the square of a fair number. An
# example would be 121, because not only is it fair, it is the square
# of 11, which is also a fair number.
#
# Your task is, given an interval Little John is searching through, to
# tell him how many fair and square numbers are there in the interval,
# so he knows when he has found them all.

import math

FILE_NAME = "C-small-attempt0.in"
OUTPUT = "fair_sq.out"

def load_file():
    '''open text file and insert each line into a list'''
    in_file = open(FILE_NAME, 'r', 0)
    line_list = list(in_file)
    in_file.close()
    # remove all newline chars from the list of strings
    line_list = [i.strip('\n') for i in line_list]
    # convert strings to lists to make list of lists
    line_list = [line_list[i].split() for i in range(len(line_list))]
    # cast all list elements to type int
    line_list = [map(int, line_list[i]) for i in range(len(line_list))]
    return line_list

def fair_square(a, b):
    '''
    Finds how many fair numbers that are also squares of fair numbers
    exist from a to b inclusive.
    Input: integers a, b
    Returns: integer number of fair squares from a to b inclusive
    '''
    memo_fair = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66,
                77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171,
                181, 191, 202, 212, 222, 232, 242, 252, 262, 272, 282,
                292, 303, 313, 323, 333, 343, 353, 363, 373, 383, 393,
                404, 414, 424, 434, 444, 454, 464, 474, 484, 494, 505,
                515]
    f_cnt = 0
    for num in xrange(a, b+1):
        sqrt = (num**0.5)
        if abs(sqrt - round(sqrt)) < 0.00001:
            sqrt = int(round(sqrt))
        else:
            sqrt = -1
        str_sqrt = str(sqrt)
        if num in [0, 1, 4, 9, 121, 484]:
            f_cnt += 1
        elif (sqrt in memo_fair and str(num) == str(num)[::-1]):
            #print sqrt, num
            f_cnt += 1
    return f_cnt

input_list = load_file()
output_file = open(OUTPUT, 'w')
num_cases = int(input_list.pop(0)[0])
case_cnt = 1
for case in range(num_cases):
    ans = fair_square(input_list[case][0], input_list[case][1])
    output_file.write('Case #' + str(case_cnt) + ': ' + str(ans) + '\n')
    case_cnt += 1
output_file.close()
