#!/usr/bin/env python

import sys


def handle_case(case, k):
    case_arr = map(lambda x: x == '+', list(case))
    count = 0
    length = len(case_arr)
    while True:
        first_false_idx = next((i for i, v in enumerate(case_arr) if not v), -1)
        if first_false_idx == -1:
            return count
        if first_false_idx + k <= length:
            for i in range(first_false_idx, first_false_idx + k):
                case_arr[i] = not case_arr[i]
            count = count + 1
        else: 
            return 'IMPOSSIBLE'


with open(sys.argv[1], 'r') as my_file:
    first  = True
    num_lines = 0
    count = 1
    for line in my_file:
        if first:
            first = False
            num_lines = int(first)
        else :
            [case, k] = line.split(' ')
            print('Case #%d: %s' % (count, str(handle_case(case, int(k.strip())))))
            count = count + 1
