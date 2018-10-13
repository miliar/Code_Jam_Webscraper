#!/usr/bin/python

import re
import sys


input_file = open('A-large.in')
output_file = open('A-large.out', 'w')

T = int(input_file.readline())

for t in range(T):
    (N, K) = map(int, input_file.readline().split(' '))
    k = K % (2 ** N)
    result = True
    for i in range(N):
        if(not (k & (2 ** i))):
            result = False
    if result:
        output_file.write("Case #" + str(t + 1) + ": ON\n")
    else:
        output_file.write("Case #" + str(t + 1) + ": OFF\n")


input_file.close()
output_file.close()
