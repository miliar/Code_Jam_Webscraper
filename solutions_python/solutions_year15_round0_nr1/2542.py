#!/usr/bin/env python
#coding: utf-8

# problem A: Standing Ovation

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', type=str, default='A-small.in', help='input data file')
args = parser.parse_args()

f = open(args.input)
case_num = int(f.readline())
output = []

for c in range(case_num):
    sp = f.readline().split(' ')
    shy_num = int(sp[0]) + 1
    nums = []
    for i in range(shy_num):
        nums.append(int(sp[1][i]))

    standing_people = 0
    invited_friends = 0
    for s in range(len(nums)):
        while standing_people < s:
            invited_friends += 1
            standing_people += 1
        standing_people += nums[s]
    output.append(invited_friends)

fo = open('a.out', 'w')
for i in range(len(output)):
    s = 'Case #' + str(i+1) + ': ' + str(output[i])
    # print(s)
    fo.write(s + '\n')

