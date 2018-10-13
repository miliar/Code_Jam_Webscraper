#!/usr/bin/env python3
import sys


def print_stalls(s: list):
    print('|' + 'x'.join(['.' * i for i in s]) + '|', file=sys.stderr)


def find_stall(s: list):
    index = s.index(max(s))
    left = (s[index] - 1) // 2
    right = s[index] - 1 - left
    new_stalls = s[:index] + [left, right] + s[index + 1:]
    return new_stalls, left, right


for case_num in range(int(input())):
    num_stalls, people_to_enter = input().split()
    num_stalls, people_to_enter = int(num_stalls), int(people_to_enter)
    print('performing test case #%d (#stalls=%d, #people=%d)' % (case_num + 1, num_stalls, people_to_enter),
          file=sys.stderr)
    stalls = [num_stalls]
    for i in range(people_to_enter - 1):
        stalls = find_stall(stalls)[0]
    # print_stalls(stalls)
    stalls, left, right = find_stall(stalls)
    # print_stalls(stalls)
    print('Case #%d: %d %d' % (case_num + 1, max(left, right), min(left, right)))
