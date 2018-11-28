#!/usr/bin/python

import re
import sys

input_file = open('A-large.in')
output_file = open('A-large.out', 'w')

T = int(input_file.readline())

for t in range(T):
    
    O = []
    B = []
    order = []
    
    line = input_file.readline().split(' ')
    N = int(line.pop(0))
    Oneeded_time = 0
    Bneeded_time = 0
    Opos = 1
    Bpos = 1
    time = 0
    for n in range(N):
        R = line.pop(0)
        order.append(R)
        P = int(line.pop(0))
        if R == 'O':
            if Bneeded_time >= abs(P-Opos):
                Oneeded_time += 1
                time += 1        
            else:
                Oneeded_time += abs(P-Opos) + 1 - Bneeded_time   
                time +=  abs(P-Opos) + 1 - Bneeded_time
            Bneeded_time = 0
            Opos = P
        else:
            if Oneeded_time >= abs(P-Bpos):
                Bneeded_time += 1
                time += 1        
            else:
                Bneeded_time += abs(P-Bpos) + 1 - Oneeded_time   
                time += abs(P-Bpos) + 1 - Oneeded_time
            Oneeded_time = 0
            Bpos = P

    output_file.write("Case #" + str(t + 1) + ": " + str(time) + "\n")

input_file.close()
output_file.close()
