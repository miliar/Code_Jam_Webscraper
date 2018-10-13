#!/usr/bin/python

"""Code Jam 2014 Qualification Round 2014"""

import sys

def cal_time(idx, c, f, x):
    """docstring for cal_time"""
    #print idx, c, f, x
    n = int(x/c - 2/f)
    if n < 1:
        n = 0
    total = 0.0
    for i in range(n):
        total += c / (2.0 + i*f)
    total += x / (2.0 + n*f)
    print "Case #%d: %.7f" % (idx, total)

def main():
    """entry point"""
    input = sys.stdin.readlines()
    case_num = int(input[0])
    for i in range(case_num):
        line = input[i + 1].strip()
        sub_strs = line.split()
        cal_time(i+1, float(sub_strs[0]), float(sub_strs[1]), float(sub_strs[2]))


if __name__ == '__main__':
    main()
