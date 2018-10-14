#!/usr/bin/env python

import sys, fractions, functools

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
        
def solve(N, M, lawn):
    if N == 1 or M == 1:
        return "YES"
    
    linemax = [0 for i in range(N)]
    colmax = [0 for j in range(M)]
    
    invlawn = [[0] * N] * M
    for j in range(M):
        invlawn[j] = [0 for i in range(N)]
        for i in range(N):
            invlawn[j][i] = lawn[i][j]
            
    for j in range(M):
        colmax[j] = max(invlawn[j])  
    for i in range(N):    
        linemax[i] = max(lawn[i])
    
    for i in range(N):
        for j in range(M):
            if lawn[i][j] < linemax[i] and lawn[i][j] < colmax[j]:
                return "NO"
    
    return "YES"

inputfilename = sys.argv[1]
inputfile = open(inputfilename, "r")

## parse file
## drop first line
line = inputfile.readline()
case = 1

for line in inputfile:
    args = line.split(' ')
    N = int(args[0])
    M = int(args[1])
    lawn = [[0] * M] * N
    for i in range(N):
        lawn[i] = [0 for j in range(M)]
        line = inputfile.readline()
        args = line.split(' ')
        for j in range(M):
            lawn[i][j] = int(args[j])
                
    #print_mat(N, lawn)
    result = solve(N, M, lawn)
    print("Case #%d: %s" % (case, result))
    case = case + 1