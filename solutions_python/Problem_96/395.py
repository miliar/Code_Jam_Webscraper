#!/usr/bin/python

import re
import sys
from math import floor, ceil

input_file = open('B-large.in')
output_file = open('B-large.out', 'w')

T = int(input_file.readline())

def generate_sets(n):
    mean = n/3.0
    dec = mean - floor(mean)
    if n == 0:
        return ((0,0,0),)
    if n == 1:
        return ((1,0,0),)
    if n == 30:
        return ((10,10,10),)
    if n == 29:
        return ((10,10,9),)
    if dec < 0.1:
        return ((int(floor(mean)), int(floor(mean)), int(floor(mean))), 
                (int(floor(mean)+1), int(floor(mean)-1), int(floor(mean))))
    elif dec < 0.5:
        return ((int(ceil(mean)), int(floor(mean)), int(floor(mean))), 
                (int(floor(mean)+1), int(floor(mean)-1), int(ceil(mean))))
    else:
        return ((int(ceil(mean)), int(ceil(mean)), int(floor(mean))),
                (int(ceil(mean)+1), int(floor(mean)), int(ceil(mean)-1)))

for t in range(T):
    
    
    line = map(int, input_file.readline().split(' '))
    N = line[0]
    S = line[1]
    p = line[2]
    n = line[3:]
    
    result = 0
    
    for number in n:
        sets = generate_sets(number)
        if sets[0][0] >= p:
            result += 1
            continue
        if S > 0 and len(sets) > 1 and sets[1][0] >= p:
            S -= 1
            result += 1
    
    output_file.write("Case #" + str(t + 1) + ": " + str(result) + "\n")

input_file.close()
output_file.close()
