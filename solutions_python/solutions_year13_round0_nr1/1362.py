#!/usr/bin/env python

import sys

with open(sys.argv[1]) as f_in:
    lines = f_in.readlines()
    lines = [x.strip() for x in lines]

T = int(lines[0])

mapping = {
    0:  'Draw',
    1:  'Game has not completed',
    2:  'O won',
    3:  'X won',
}

def countchar(line, char):
    return sum([1 if x==char else 0 for x in line])

def checkline(line):
    #print "checking ", line
    if countchar(line, 'X') == 4:
        return 3
    if countchar(line, 'X') == 3 and 'T' in line:
        return 3
    if countchar(line, 'O') == 4:
        return 2
    if countchar(line, 'O') == 3 and 'T' in line:
        return 2
    if '.' in line:
        return 1
    return 0

for i in range(0, T):
    data = "".join(lines[(i*5)+1:(i*5)+5])
    #print i*5+1, i*5+5
    #print i, data, len(data)

    result = 0

    comp_lines = ([data[0+j]+data[4+j]+data[8+j]+data[12+j] for j in range(0, 4)] +
            [data[j*4]+data[j*4+1]+data[j*4+2]+data[j*4+3] for j in range(0, 4)] +
            [data[0]+data[5]+data[10]+data[15]] +
            [data[3]+data[6]+data[9]+data[12]])

    for line in comp_lines:
        result = max(result, checkline(line))

    print "Case #%d: %s" % (i+1, mapping[result])
    
