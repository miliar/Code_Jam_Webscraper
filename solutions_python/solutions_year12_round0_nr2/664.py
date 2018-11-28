# -*- coding: utf-8 -*-
import sys

input_file = open(sys.argv[1], 'r')
output_file = open(sys.argv[2], 'w')

input_file.readline()

for i, s in enumerate(input_file.readlines()):
    L = s.split()
    L.pop(0)
    surprise_count = int(L.pop(0))
    p = int(L.pop(0))
    res = 0
    score_list = [int(x) for x in L]
    for t in score_list:
        if t >= 3*p - 2:
            res += 1
        elif surprise_count and t >= 3*p - 4 and t >= p:
            res += 1
            surprise_count -= 1
    output_file.writelines("Case #{0}: {1}\n".format(i+1, res))