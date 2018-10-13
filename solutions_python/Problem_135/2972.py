#!/usr/bin/env python
# -*- coding: utf-8 -*-

input = open("input.txt", "r")
output = open("output.txt", "w")

t = int(input.readline().strip())
for i in range(t):
    row1 = int(input.readline().strip())
    for j in range(4):
        test = map(int, input.readline().strip().split())
        if j + 1 == row1:
            matrix1 = test
    row2 = int(input.readline().strip())
    for j in range(4):
        test = map(int, input.readline().strip().split())
        if j + 1 == row2:
            matrix2 = test
    matrix1, matrix2 = set(matrix1), set(matrix2)
    s = matrix1 & matrix2
    l = len(s)
    if l == 0:
        str = 'Case #%d: Volunteer cheated!' % (i + 1)
    elif l > 1:
        str = 'Case #%d: Bad magician!' % (i + 1)
    elif l == 1:
        str = 'Case #%d: %d' % (i + 1, s.pop())
    output.write(str + "\n")

input.close()
output.close()
