# -*- coding: utf-8 -*-
"""
Created on Sat Apr 08 00:22:49 2017

@author: Miguel
"""

import sys

def oversizedPancakeFlipper(row, k):
    row = [x for x in row]
    pos = 0
    moves = 0
    while pos < len(row):
        
        if row[pos] == "-":
            #print row
            moves += 1
            if pos + k > len(row):
                return "IMPOSSIBLE"
            for i in range(pos, pos + k):
                if row[i] == "+":
                    row[i] = "-"
                else:
                    row[i] = "+"
            #print row, "new"
        pos += 1
    return moves
        

counter = 0

for line in sys.stdin:
    if counter == 0:
        counter += 1
        n_cases = int(line)
        continue
    line = line.split(" ")
    row = line[0]
    k = int(line[1])
    print "Case #" + str(counter) + ": " + str(oversizedPancakeFlipper(row, k))
    counter += 1