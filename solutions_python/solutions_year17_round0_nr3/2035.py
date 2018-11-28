#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import math

try:
    input_file = sys.argv[1]
except:
    input_file = sys.argv[0].split(".")[0] +  ".in"

output_file = input_file.split(".")[0] + ".out"

f = open(input_file, 'r')
fo = open(output_file, 'w')

T = int(f.readline())

def solve(stalls,k):
    last = 0
    for i in range(k):
        emptys = [0]* len(stalls)
        c = 0
        inx = 0
        for j in range(len(stalls)):
            if stalls[j] == 1:
                emptys[inx+1] = c
                emptys[j] = 0
                inx = j
                c = 0
            if stalls[j] == 0:
                c+=1
        m = max(emptys)
        i = emptys.index(m)
        indice = int(i + math.ceil(m/2.0) -1)
        stalls[indice] = 1
        last = indice
    l = 0
    r = 0
    i = last
    while i>=0:
        i -= 1
        if stalls[i] == 0:
            l += 1
        else:
            break
    i = last
    while i<=len(stalls):
        i += 1
        if stalls[i] == 0:
            r += 1
        else:
            break
    return max(r,l),min(r,l)

for i in range(T):
    case = f.readline().strip()
    N, k = map(int, case.split(" "))

    stalls = [1] + N*[0] + [1]
    out_case = solve(stalls,k)
    a,b = out_case

    print "Case #" + str(i + 1) + ": " + str(a) + " " + str(b)
    fo.write("Case #" + str(i + 1) + ": " + str(a) + " " + str(b) + '\n')
