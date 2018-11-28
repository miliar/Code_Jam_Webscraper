#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def solve(case):
    # base_elements = [ "Q", "W", "E", "R", "A", "S", "D", "F" ]
    (comb, op, invoked) = case
    
    combine = {}
    for e in comb:
        combine[tuple(sorted((e[0], e[1])))] = e[2]
    
    opposed = {}
    for e in op:
        opposed[e[0]] = e[1]
        opposed[e[1]] = e[0]

    result = []
    for e in invoked:
        if len(result) == 0:
            result = [e]
            continue
        
        pair = tuple(sorted((e, result[-1])))
        if pair in combine:
            result[-1] = combine[pair]
        elif e in opposed and opposed[e] in result:
            result = []
        else:
            result.append(e)
    
    return result
    
def readfile(file):
    f = open(file, "r")

    T = int(f.readline())
    data = []
    for line in f:
        case = line.split()
        p = 0

        C = int(case[p])
        p += 1
        combine = []
        for i in range(C):
            combine.append(case[p])
            p += 1

        D = int(case[p])
        p += 1
        opposed = []
        for i in range(D):
            opposed.append(case[p])
            p += 1
        
        N = int(case[p])
        p += 1
        invoked = case[p]
        
        # print(C, combine, D, opposed, N, invoked)
        data.append([combine, opposed, invoked])
    f.close()

    if len(data) != T:
        print("Wrong number of data read. T = %d, actual = %d" % (T, len(data)))
        sys.exit(1)
        
    return data

#
# main
#
if len(sys.argv) > 1:
    file = sys.argv[1]
else:
    file = "sample.in"
output = open(file + ".out", "w")

cases = readfile(file)
n = 1
for case in cases:
    result = "["
    for i in solve(case):
        result += i + ", "
    if len(result) > 1:
        result = result[:-2]
    result += "]"
    msg = "Case #%d: %s" % (n, result)
    print(msg)
    output.write(msg + "\n")
    n += 1

output.close()
        