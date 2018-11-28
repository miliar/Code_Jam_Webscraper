#!/usr/bin/python

import sys

def do_each(case_num):
    first_round_row = int(sys.stdin.readline())
    for i in range(4):
        s = sys.stdin.readline()
        if i == (first_round_row - 1):
            possibles1 = map(int, s.strip().split())
    second_round_row = int(sys.stdin.readline())
    for i in range(4):
        s = sys.stdin.readline()
        if i == (second_round_row - 1):
            possibles2 = map(int, s.strip().split())
    possibles = list(set(possibles1) & set(possibles2))
    if len(possibles) == 1:
        msg = str(possibles[0])
    if len(possibles) < 1:
        msg = 'Volunteer cheated!'
    if len(possibles) > 1:
        msg = 'Bad magician!'
    sys.stdout.write("Case #{}: {}\n".format(case_num+1, msg))

def do_all():
    num_cases = int(sys.stdin.readline())
    for i in range(num_cases):
        do_each(i)


do_all()


