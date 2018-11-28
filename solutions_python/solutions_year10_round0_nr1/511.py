#!/usr/bin/python
# *-* coding: UTF-8 -*-

input_file = file('A-large.in')
output_template = "Case #%d: %s"
T = int(input_file.readline())

for i in xrange(T):
    index = i + 1
    line = input_file.readline().split()
    N = int(line[0])
    K = int(line[1])

    two_pow_N = 2 ** N

    if ((K+1) % two_pow_N) == 0:
        result = "ON"
    else:
        result = "OFF"

    print output_template % (index, result)

