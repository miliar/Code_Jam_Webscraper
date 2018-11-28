#!/usr/bin/python3

import fileinput
from collections import deque
from collections import OrderedDict
from math import log
from math import floor
from math import ceil

f = fileinput.input()
T = int(f.readline())


for case in range(T):

    R, C = map(int, f.readline().strip().split())

    matrix = []
    for x in range(R):
        row  = [c for c in f.readline().strip()]
        matrix.append(row)

    prow = C * ['']
    
    for i in range(R):
        prev  = ''
        for k in range(C):
            a = matrix[i][k]
            if a == '?' and prev != '':
                matrix[i][k] = prev
            prev = matrix[i][k]

    for i in range(R):
        prev  = ''
        for k in range(C - 1, -1, -1):
            a = matrix[i][k]
            if a == '?' and prev != '':
                matrix[i][k] = prev
            prev = matrix[i][k]

    prev  = []

    for i in range(R):
        if matrix[i][0] == '?' and prev != []:
           matrix[i] = prev
        prev = matrix[i]

    prev  = []

    for i in range(R - 1, -1, -1):
        if matrix[i][0] == '?' and prev != []:
           matrix[i] = prev
        prev = matrix[i]


    print("Case #" + str(case + 1) + ":")
    for row in matrix:
        print(''.join(row))

