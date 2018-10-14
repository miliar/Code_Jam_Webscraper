#!/usr/bin/env python

import sys

def Solve(choice1, choice2, table1, table2):
    s1 = set(table1[choice1-1].split())
    s2 = set(table2[choice2-1].split())
    si = s1 & s2
    if len(si) == 1: return list(si)[0]
    elif len(si) > 1: return "Bad magician!"
    else: return "Volunteer cheated!"

inp = open(sys.argv[1], 'r').readlines()
T = int(inp[0].strip())
line = 0
for t in range(T):
    choice1 = int(inp[line+1].strip())
    table1 = inp[line+2:line+6]
    choice2 = int(inp[line+6].strip())
    table2 = inp[line+7:line+11]
    print "Case #"+str(t+1)+": "+Solve(choice1, choice2, table1, table2)
    line += 10


    
