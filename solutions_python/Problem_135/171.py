#!/usr/bin/python
# coding: UTF-8

# Input

# The first line of the input gives the number of test cases, T. T test cases follow. Each test case starts with a line containing an integer: the answer to the first question. The next 4 lines represent the first arrangement of the cards: each contains 4 integers, separated by a single space. The next line contains the answer to the second question, and the following four lines contain the second arrangement in the same format.
# Output

# For each test case, output one line containing "Case #x: y", where x is the test case number (starting from 1).

# If there is a single card the volunteer could have chosen, y should be the number on the card. If there are multiple cards the volunteer could have chosen, y should be "Bad magician!", without the quotes. If there are no cards consistent with the volunteer's answers, y should be "Volunteer cheated!", without the quotes. The text needs to be exactly right, so consider copying/pasting it from here.
# Limits

# 1 ≤ T ≤ 100.
# 1 ≤ both answers ≤ 4.
# Each number from 1 to 16 will appear exactly once in each arrangement.


def check(cases):
    ans = []
    f_row = int(cases[0])
    s_row = int(cases[5])
    print s_row
    f_case = cases[f_row].split(' ')
    s_case = cases[5+s_row].split(' ')
    for x in f_case:
        if x in s_case:
            ans.append(x)
            if len(ans) > 1:
                return "Bad magician!"
    if len(ans) == 0:
        return "Volunteer cheated!"
    return str(ans[0])

txtfile = open('A-small-attempt0.in').read()
# print txtfile
cases = txtfile.split('\n')

case_num = int(cases[0])

obj = open("a_small_ans.txt", "w")

for a in range(case_num):
    start = (a)*10+1
    end = (a)*10+11
    print >>obj, 'Case #'+str(a+1)+': '+check(cases[start:end])
