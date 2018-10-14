#!/usr/bin/python

import re
import sys

input_file = open('A-large.in')
output_file = open('A-large.out', 'w')
#output_file = sys.stdout

T = int(input_file.readline())



def intersect(w1, w2):
    if (w1[0] > w2[0] and w1[1] < w2[1]) or (w1[0] < w2[0] and w1[1] > w2[1]):
        return True
    else:
        return False

for t in range(T):
    N = int(input_file.readline())
    i = 0
    wires = []
    while i < N:
        wires.append(map(int, input_file.readline().split(' ')))
        i += 1

    i = 0
    count = 0
    while i < N - 1:
        u = i + 1
        while u < N:
            if intersect(wires[i], wires[u]):
                count += 1
            u += 1
        i += 1


    output_file.write("Case #" + str(t + 1) + ": " + str(count) + "\n")

input_file.close()
output_file.close()
