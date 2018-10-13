#!/usr/bin/env python
# coding=utf-8

# Last modified: <2012-04-14 14:25:59 Saturday by richard>

# @version 0.1
# @author : Richard Wong
# Email: chao787@gmail.com


import sys

def main(lines):
    line_list = lines.split("\n")
    lineno = int(line_list[0])
    for i in range(1, lineno + 1):
        result = process_line(line_list[i])
        print "Case #%d: %d" % (i, result)

    return

def process_line(line):
    line_list = line.split()
    N = int(line_list[0])
    S = int(line_list[1])
    P = int(line_list[2])
    result = 0
    for i in range(3, N + 3):
        num = int(line_list[i])
        if process_num(num, P) == 2:
            result += 1
        elif process_num(num, P) == 1:
            if S != 0:
                S -= 1
                result += 1
    return result

def process_num(num, P):
    if common_num(num) >= P:
        # no surprise and get P
        return 2
    elif surprise_num(num) >= P:
        # surprise and get P
        return 1
    else:
        # cannot get P
        return 0

def common_num(num):
    if num % 3 == 0:
        return num / 3
    else:
        return num / 3 + 1


def surprise_num(num):
    if num == 0:
        return 0
    if num % 3 == 2:
        return num / 3 + 2
    else:
        return num / 3 + 1

def will_surprise(num):
    if num % 3 == 1:
        return False
    else:
        return True


if __name__ == '__main__':
    assert len(sys.argv) == 2
    filename = sys.argv[1]
    with open(filename, "r") as f:
        main(f.read())



