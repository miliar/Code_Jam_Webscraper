#!/usr/bin/python

"""Code Jam 2014 Qualification Round 2014"""

import sys

def check_magic(idx, first_line, second_line):
    """check the magic correctness"""
    ret = []
    for val in first_line:
        if val in second_line:
            ret.append(val)
    if ret:
        if len(ret) is 1:
            ret_str = "%d" % ret[0]
        else:
            ret_str = "Bad magician!"
    else:
        ret_str = "Volunteer cheated!"
    print "Case #%d: %s" % (idx, ret_str)

def main():
    """entry point"""
    input = sys.stdin.readlines()
    case_num = int(input[0])
    for i in range(case_num):
        first_idx = int(input[i*10 + 1])
        line = input[i*10 + first_idx + 1].strip().split()
        first_line = [int(val) for val in line]
        second_idx = int(input[i*10 + 6])
        line = input[i*10 + second_idx + 6].strip().split()
        second_line = [int(val) for val in line]
        check_magic(i + 1, first_line, second_line)


if __name__ == '__main__':
    main()
