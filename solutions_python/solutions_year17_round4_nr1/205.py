#!/usr/bin/python

import sys
import collections
import math

if len(sys.argv) != 2:
    print "usage: %s <input_file_name>" % sys.argv[0]
    exit()

input_file_name = sys.argv[1]
if input_file_name[-3:] == ".in":
    output_file_name = input_file_name[:-3] + ".out"
else:
    output_file_name = input_file_name + ".out"

def solve(N, P, G):
    mod = [0] * P
    for g in G:
        mod[g % P] += 1
    if P == 2:
        ret = mod[0] + mod[1] / 2
        if mod[1] % 2 > 0:
            ret += 1
    elif P == 3:
        mod12 = min(mod[1], mod[2])
        ret = mod[0] + mod12 + (mod[1] + mod[2] - 2 * mod12) / 3
        if (mod[1] + mod[2] - 2 * mod12) % 3 > 0:
            ret += 1
    elif P == 4:
        mod13 = min(mod[1], mod[3])
        mod[1] -= mod13
        mod[3] -= mod13
        mod1or3 = (mod[1] + mod[3]) / 4
        mod22 = mod[2] / 2
        ret = mod[0] + mod13 + mod22 + mod1or3

        mod1or3_left = (mod[1] + mod[3]) % 4
        mod22_left = mod[2] % 2
        if mod22_left >= 1 and mod1or3_left >= 2:
            mod22_left -= 1
            mod1or3_left -= 2
            ret += 1
        if mod22_left > 0 or mod1or3_left > 0:
            ret += 1
    return ret

results = []
with open(input_file_name, 'r') as f:
    T = int(f.readline())
    for i in xrange(T):
        line = f.readline().strip('\n')
        N, P = [int(x) for x in line.split(' ')]
        line = f.readline().strip('\n')
        G = [int(x) for x in line.split(' ')]
        ret = solve(N, P, G)
        results.append(str(ret))
        output_string = "Case #%d: %s\n" % (len(results), results[-1])
        print output_string[:-1]

with open(output_file_name, 'w') as f:
    for i in range(len(results)):
        output_string = "Case #%d: %s\n" % (i + 1, results[i])
        f.write(output_string)
