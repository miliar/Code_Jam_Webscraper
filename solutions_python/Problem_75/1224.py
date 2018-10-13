#!/usr/bin/env python


import sys
import math

def get_special_letters(line):
    combine = {}
    opposed = {}

    num_combined = int(line[0])
    next_i = 0
    if num_combined > 0:
        next_i += num_combined + 1
        for i in range(1, num_combined + 1):
            comb = line[i]
            key = ''.join(sorted(comb[0:2]))
            value = comb[2]
            combine[key] = value
    else:
        next_i = 1
    num_opposed = int(line[next_i])
    if num_opposed > 0:
        for i in range(next_i + 1, next_i + num_opposed + 1):
            opp = line[i]
            opposed[opp[0]] = opp[1]
            opposed[opp[1]] = opp[0]
        next_i += num_opposed + 1
    else:
        next_i += 1
    invoked = list(line[next_i + 1])
    return combine, opposed, invoked



def invoke(line):
    combine, opposed, invoked = get_special_letters(line)
    result = []
    for inv in invoked:
        result.append(inv)
        comb_key = ''.join(sorted(result[-2:]))
        if comb_key in combine.keys():
            result = result[0:-2]
            result.append(combine[comb_key])
        elif inv in opposed.keys():
            opp = opposed[inv]
            if opp in result:
                result = []
    return result
    

line_num = int (sys.stdin.readline())
lines = []
for i in range(0, line_num):
    lines.append(sys.stdin.readline().strip())
lines = [l.split() for l in lines]
i = 1
for line in lines:
    res = invoke(line)
    res = ', '.join(res)
    print 'Case #%d: [%s]' %(i, res)
    i += 1