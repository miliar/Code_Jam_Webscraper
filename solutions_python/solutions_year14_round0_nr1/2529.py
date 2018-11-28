#!/usr/bin/python
# vi: set fileencoding=utf-8 :

import math

def judge(first_row, second_row): 
    join = set(first_row) & set(second_row)
    if len(join) == 0:
        return 'Volunteer cheated!'
    elif len(join) == 1:
        return list(join)[0]
    else:
        return 'Bad magician!'


T = int(raw_input())
for t in range(T):
    first_row_number = int(raw_input())
    for r in range(1, 5):
        row = raw_input()
        if r != first_row_number:
            continue
        first_row = row.split(' ')
        for c in range(4):
            first_row[c] = int(first_row[c])
    second_row_number = int(raw_input())
    for r in range(1, 5):
        row = raw_input()
        if r != second_row_number:
            continue
        second_row = row.split(' ')
        for c in range(4):
            second_row[c] = int(second_row[c])
    print 'Case #' + str(t + 1) + ':', judge(first_row, second_row)
