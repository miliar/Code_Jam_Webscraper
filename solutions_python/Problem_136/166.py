#!/usr/bin/python
# coding: UTF-8

# Input

# The first line of the input gives the number of test cases, T. T lines follow. Each line contains three space-separated real-valued numbers: C, F and X, whose meanings are described earlier in the problem statement.

# C, F and X will each consist of at least 1 digit followed by 1 decimal point followed by from 1 to 5 digits. There will be no leading zeroes.
# Output

# For each test case, output one line containing "Case #x: y", where x is the test case number (starting from 1) and y is the minimum number of seconds it takes before you can have X delicious cookies.

# We recommend outputting y to 7 decimal places, but it is not required. y will be considered correct if it is close enough to the correct number: within an absolute or relative error of 10-6. See the FAQ for an explanation of what that means, and what formats of real numbers we accept.
# Limits

# 1 ≤ T ≤ 100.
# Small dataset

# 1 ≤ C ≤ 500.
# 1 ≤ F ≤ 4.
# 1 ≤ X ≤ 2000.
# Large dataset

# 1 ≤ C ≤ 10000.
# 1 ≤ F ≤ 100.
# 1 ≤ X ≤ 100000.


# def f_time(C, F, iteration):
#     if iteration == 0:
#         return 0
#     return C / (2.0 + F * (iteration - 1)) + f_time(C, F, iteration - 1)


def min_time(C, F, X):
    iteration = 0
    f_time = 0
    now = X/2
    while True:
        f_time = f_time + C / (2 + F * iteration)
        # now = X / (2 + F * iteration) + f_time
        next = X / (2 + F * (iteration + 1)) + f_time
        if now < next:
            return str(round(now, 7))
        now = next
        iteration = iteration + 1

# txtfile = open('B-small-attempt1.in').read()
txtfile = open('B-large.in').read()
# txtfile = open('test_b.txt').read()
cases = txtfile.split('\n')

case_num = int(cases[0])

obj = open("b_large_ans.txt", "w")

for a in range(case_num):
    inputs = cases[a+1].split()
    C = float(inputs[0])
    F = float(inputs[1])
    X = float(inputs[2])
    print >> obj, 'Case #'+str(a+1)+': '+min_time(C, F, X)
