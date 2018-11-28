#!/usr/bin/env python

import sys

def print_array(a):
    if len(a) == 0:
        print("[]")
    else:
        print("[", end = "")
        for i in range(len(a)-1):
            print("%s, " % (a[i]), end = "")
        print("%s]" % (a[len(a)-1]))

def print_mat(N, mat):
    for i in range(N):
        print_array(mat[i])
        #print("".join(mat[i]))

def solve(table):
    # diagonal
    if table[0][0] != '.':
        seq = True
        if table[0][0] =='T':
            for i in [2, 3]:
                seq = seq and table[i][i] == table[1][1]
            if seq:
                return "%s won" % table[1][1]
        else:
            for i in [1, 2, 3]:
                seq = seq and (table[i][i] == table[0][0] or table[i][i] == 'T')
            if seq:
                return "%s won" % table[0][0]
    
    # reverse diagonal
    if table[0][3] != '.':
        seq = True
        if table[0][3] =='T':
            for i in [2, 3]:
                seq = seq and table[i][3-i] == table[1][2]
            if seq:
                return "%s won" % table[1][2]
        else:
            for i in [1, 2, 3]:
                seq = seq and (table[i][3-i] == table[0][3] or table[i][3-i] == 'T')
            if seq:
                return "%s won" % table[0][3]
    
    for i in range(4):
        # lines
        if table[i][0] != '.':
            seq = True
            if table[i][0] =='T':
                for j in [2, 3]:
                    seq = seq and table[i][j] == table[i][1]
                if seq:
                    return "%s won" % table[i][1]
            else:
                for j in [1, 2, 3]:
                    seq = seq and (table[i][j] == table[i][0] or table[i][j] == 'T')
                if seq:
                    return "%s won" % table[i][0]     
    
        # columns
        if table[0][i] != '.':
            seq = True
            if table[0][i] =='T':
                for j in [2, 3]:
                    seq = seq and table[j][i] == table[1][i]
                if seq:
                    return "%s won" % table[1][i]
            else:
                for j in [1, 2, 3]:
                    seq = seq and (table[j][i] == table[0][i] or table[j][i] == 'T')
                if seq:
                    return "%s won" % table[0][i]     
    
    full = True
    for i in range(4):
        for j in range(4):
            full = full and table[i][j] != '.'
    
    if(full):
        return "Draw"
    else:
        return "Game has not completed"

inputfilename = sys.argv[1]
inputfile = open(inputfilename, "r")

## parse file
## drop first line
line = inputfile.readline()
case = 1

for line in inputfile:
    table = [[0] * 4] * 4
    for i in range(4):
        table[i] = ['.' for j in range(4)]
        for j in range(4):
            table[i][j] = line[j] 
        line = inputfile.readline()
                
    #print_mat(4,table)
    result = solve(table)
    print("Case #%d: %s" % (case, result))
    
    case = case + 1