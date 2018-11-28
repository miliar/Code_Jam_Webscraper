#!/usr/bin/env python3
# -*- coding: utf-8 -*-

inputFile = open('B-small-attempt0.in.txt', 'r', encoding='utf-8')
outputFile = open('output.txt', 'w', encoding='utf-8')

T = int(inputFile.readline().strip())
for _ in range(T):
    line = inputFile.readline().strip().split(' ')
    line = [int(value) for value in line]
    N = line[0]
    S = line[1]
    p = line[2]
    
    out = 0
    p3 = 3 * p
    
    if p == 0:
        out = N
        outputFile.write("Case #" + str(_ + 1) + ": " + str(out) + "\n")
        continue

    for i in range(N):
        ti = line[i + 3]
        
        if ti == 0:
            continue
        if ti == 1:
            if p == 1:
                out += 1
                continue
            else:
                continue
        
        if p3 <= ti + 2:
            out += 1
        else:
            if S > 0:
                if p3 <= ti + 4:
                    out += 1
                    S -= 1
         
    outputFile.write("Case #" + str(_ + 1) + ": " + str(out) + "\n")
    print(out)
