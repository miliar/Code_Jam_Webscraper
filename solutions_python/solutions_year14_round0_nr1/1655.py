#!/usr/bin/python
#
# author: tzeng.yuxio@gmail.com
# usage: cat file.input | ./qround-problem-a.py > file.output

import sys

def get_a_row():
    a = (int)(sys.stdin.readline())
    b = 5 - a
    while a > 1:
        sys.stdin.readline()
        a -= 1
    s = sys.stdin.readline()
    while b > 1:
        sys.stdin.readline()
        b -= 1

    return s[:-1].split()

def solve():
    s1 = get_a_row()
    s2 = get_a_row()
    c  = [x for x in s1 if x in s2]

    if len(c) == 1:
        return c[0]
    elif len(c) == 0:
        return "Volunteer cheated!"
    else:
        return "Bad magician!"

t = (int)(sys.stdin.readline())
for i in range(t):
    print 'Case #' + repr(i+1) + ': ' + solve()
