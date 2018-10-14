__author__ = 'fcueto'
# Copyright 2014 Fernando Gonzalez del Cueto. Subject to the MIT License.
# Google Code Jam Round 1B 2014
# Problem B: New Lottery Game


import numpy as np

file_in  = 'B-small-attempt1.in'
file_out = file_in.replace('.in', '.out')
fid_in  = open(file_in, 'r')
fid_out = open(file_out,'w')

N_cases = int(fid_in.readline().strip())

for i in range(N_cases):

    def_line = [int(x) for x in fid_in.readline().strip().split() ]
    A = def_line[0]
    B = def_line[1]
    K = def_line[2]

    count = 0;
    for j1 in range(A):
        for j2 in range(B) :
            if (j1 & j2) < K:
                count = count + 1

    line = "Case #%i: %i\n" % (i+1, count)
    print(line.strip())
    fid_out.write(line)

fid_in.close()
fid_out.close()
