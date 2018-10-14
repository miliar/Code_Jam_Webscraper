#!/usr/bin/env python

import sys, fractions, functools

def printmat(N, mat):
    for i in range(N):
        print("".join(mat[i]))
        
def print_array(a):
    if len(a) == 0:
        print("[]")
    else:
        print("[", end = "")
        for i in range(len(a)-1):
            print("%s, " % (a[i]), end = "")
        print("%s]" % (a[len(a)-1]))

# element_to_int
def eti(b):
    if b == 'Q': return 0
    if b == 'W': return 1
    if b == 'E': return 2
    if b == 'R': return 3
    if b == 'A': return 4
    if b == 'S': return 5
    if b == 'D': return 6
    if b == 'F': return 7
    return 8

def is_opposed(elist, e, opposed):
    for f in elist:
        if opposed[eti(e)][eti(f)]:
            return True
    return False
 
def solve(C, D, N, combos, opposed, deck):
    elist = []
    for e in deck:
        elist.append(e)
        if len(elist) >= 2:
            u = elist[-2]
            if(combos[eti(e)][eti(u)] != '0'):
                elist.pop()
                elist.pop()
                elist.append(combos[eti(e)][eti(u)])
                
            elif is_opposed(elist, e, opposed):
                elist = []
                
    return elist

inputfilename = sys.argv[1]
inputfile = open(inputfilename, "r")

## parse file
## drop first line
line = inputfile.readline()
case = 1

for line in inputfile:
    args = line.split(' ')
    C = int(args[0])
    D = int(args[C+1])
    N = int(args[C+D+2])
    comb = args[1:C+1]
    oppo = args[C+2:C+D+2]
    deck = args[C+D+3:][0]
    if deck[-1] == '\n':
        deck = deck[:-1] # get rid of '\n'
    
    combos = [['0'] * 9] * 9
    for i in range(9):
        combos[i] = ['0' for j in range(9)]
    for x in comb:
        combos[eti(x[0])][eti(x[1])] = x[2]
        combos[eti(x[1])][eti(x[0])] = x[2]
    
    opposed = [[False] * 9] * 9
    for i in range(9):
        opposed[i] = [False for j in range(9)]
    for x in oppo:
        opposed[eti(x[0])][eti(x[1])] = True
        opposed[eti(x[1])][eti(x[0])] = True
    
    result = solve(C, D, N, combos, opposed, deck)
    print("Case #%d: " % (case), end="")
    print_array(result)
    case = case + 1