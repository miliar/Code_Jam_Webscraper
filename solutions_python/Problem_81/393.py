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
        
def solve(N, have_played, nr_played, score):
    result = [0] * N
    
    nr_won = [sum(score[i]) for i in range(N)]
    
    wp = [nr_won[i]/nr_played[i] for i in range(N)]
    
    owp = [[0] * N] * N
    for i in range(N):
        owp[i] = [0 for j in range(N)]
        #iter = [j for j in range(N) if have_played[i][j]]
        owp[i] = [(nr_won[j]-score[j][i])/(nr_played[j]-1) * have_played[i][j] for j in range(N)]
    
    owp_avg = [sum(owp[i])/nr_played[i] for i in range(N)]
    
    oowp_avg = [sum([owp_avg[j]*have_played[i][j] for j in range(N)])/nr_played[i] for i in range(N)]
    
    return [wp[i]/4 + owp_avg[i]/2 + oowp_avg[i]/4 for i in range(N)]

inputfilename = sys.argv[1]
inputfile = open(inputfilename, "r")

## parse file
## drop first line
line = inputfile.readline()
case = 1

for line in inputfile:
    args = line.split(' ')
    N = int(args[0])
    have_played = [[0] * N] * N
    nr_played = [0] * N
    score = [[0] * N] * N
    for i in range(N):
        have_played[i] = [False for j in range(N)]
        score[i] = [0 for j in range(N)]
        line = inputfile.readline()
        for j in range(N):
            if line[j] != '.':
                have_played[i][j] = 1
                nr_played[i] = nr_played[i] + 1
                score[i][j] = int(line[j])
                
    
    result = solve(N, have_played, nr_played, score)
    print("Case #%d:" % (case))
    for i in range(N):
        print(result[i])
    case = case + 1