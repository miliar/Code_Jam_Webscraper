__author__ = 'jiamimi'

import os
import sys


def process_case(case_str):
    #print case_str
    ori_audience_num = 0
    need_invite_num = 0

    for shyness_level in range(len(case_str)):
        digit = int(case_str[shyness_level])

        if digit > 0 and shyness_level > ori_audience_num:
            need_invite_num += shyness_level - ori_audience_num
            ori_audience_num += need_invite_num
        ori_audience_num += digit
    #print 'need', need_invite_num
    #print '======'
    return need_invite_num


args = sys.argv
if len(args) != 2:
    print 'error!'
    sys.exit()

path = args[1]
if not os.path.isfile(path):
    print 'error!'
    sys.exit()

input_file = open(path)
line_content = []
for line in input_file:
    line_content.append(line.strip('\n'))
# print line_content
# case_num = int(line_content[0])
# print case_num

invite_num = 0

# first num indicates the digits of second num
for i in range(1, len(line_content)):
    case = line_content[i]
    case = case.split(' ')[1]
    print 'Case #' + str(i) + ":", process_case(case)
