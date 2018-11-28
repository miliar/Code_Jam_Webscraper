"""
Written by blackk100 for Google Code Jam 2017 Qualifications

Problem

Tatiana likes to keep things tidy. Her toys are sorted from smallest to largest, her pencils are sorted from shortest
to longest and her computers from oldest to newest. One day, when practicing her counting skills, she noticed that some
integers, when written in base 10 with no leading zeroes, have their digits sorted in non-decreasing order. Some
examples of this are 8, 123, 555, and 224488. She decided to call these numbers tidy. Numbers that do not have this
property, like 20, 321, 495 and 999990, are not tidy.

She just finished counting all positive integers in ascending order from 1 to N. What was the last tidy number she
counted?

Input

The first line of the input gives the number of test cases, T. T lines follow. Each line describes a test case with a
single integer N, the last number counted by Tatiana.

Output

For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is
the last tidy number counted by Tatiana.
"""


def solve(a):
    b = a
    l = len(a)
    z = 0
    while z < l:
        i = 0
        while i < l - 1:
            if int(b) % 10 == 0:
                b = str(int(b) - 1)
                l = len(b)
            elif int(b[i + 1]) < int(b[i]):
                b = str(int(b) - 1)
                l = len(b)
            elif int(b[i + 1]) >= int(b[i]):
                i += 1
        z += 1
    return b

t = int(input())

for x in range(0, t):
    n = input()
    y = solve(n)
    print("Case #{}: {}".format(x + 1, y))
