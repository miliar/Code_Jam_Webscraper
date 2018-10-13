#!/usr/bin/env python

import sys

def read_int():
    return int(sys.stdin.readline())

def read_matrix(row):
    "reads the matrix and returns only the chosen row"
    result = ''
    for i in range(1,5):
        curr_row = sys.stdin.readline()
        if i == row:
            result = curr_row.strip()
    return [ int(x) for x in result.split(' ') ]

problems = read_int()

for p in range(1,problems+1):
    line1 = read_matrix(read_int())
    line2 = read_matrix(read_int())
    count = 0
    card = 0
    for l1 in line1:
        if l1 in line2:
            card = l1
            count += 1
    msg = ''
    if count == 0:
        msg = 'Volunteer cheated!'
    elif count == 1:
        msg = card
    else: 
        msg = 'Bad magician!'
    print 'Case #%i: %s' % (p, msg)
