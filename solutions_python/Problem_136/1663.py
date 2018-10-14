__author__ = 'fcueto'

import sys

import numpy as np
sys.setrecursionlimit(15000)
#from fractions import Fraction

file_in = 'B-small-attempt0.in'
#file_in = 'cookie1.txt'
fid_in = open(file_in, 'r')
fid_out = open('cookie_out.txt','w')

N_cases = int(fid_in.readline().strip())

def min_time(t, r, C, F, X) :

    t_no_more_farms = X/r
    t_one_more_farm   = C/r + X/(r+F)

    if t_no_more_farms < t_one_more_farm :
        return t + t_no_more_farms
    else :
        return min_time(t+C/r, r + F, C, F, X)


for case in range(0, N_cases) :

    row = fid_in.readline().strip().split()

    C = np.float64(row[0])
    F = np.float64(row[1])
    X = np.float64(row[2])
    #C = Fraction(row[0])
    #F = Fraction(row[1])
    #X = Fraction(row[2])


    answer = min_time(0, 2.0, C, F, X)


    line = "Case #%i: %s\n" % (case+1, answer)
    print(line)
    fid_out.write(line)

fid_in.close()
fid_out.close()