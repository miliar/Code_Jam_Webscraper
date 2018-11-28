#!/usr/bin/python
#
# This code was written by Norio TAKEMOTO 2014-4-11.

import numpy as np


###################################
fname_input="B-large.in"
fname_output="output_problemB_large.dat"
rate_init=2.0
###################################

def time_nomorefarm(rate_F, objective_X, numfarm):
    return objective_X/(rate_init+numfarm*rate_F) 


def solve_case(cost_C, rate_F, objective_X):
 
    numfarm = 0
    ss = cost_C/(rate_init+numfarm*rate_F) 
    d_numfarm = ss \
        + time_nomorefarm(rate_F, objective_X, numfarm+1) \
        - time_nomorefarm(rate_F, objective_X, numfarm)
    s_numfarm = 0.0
    while d_numfarm<0:
        s_numfarm += ss
        numfarm+=1
        ss = cost_C/(rate_init+numfarm*rate_F) 
        d_numfarm = ss \
            + time_nomorefarm(rate_F, objective_X, numfarm+1) \
            - time_nomorefarm(rate_F, objective_X, numfarm)

    total_time = s_numfarm + time_nomorefarm(rate_F, objective_X, numfarm)
    return total_time


infile=open(fname_input, 'r')
numcase = int(infile.readline())
vals_C=np.empty((numcase))
vals_F=np.empty((numcase))
vals_X=np.empty((numcase))
for jcase in range(numcase):
    seg = infile.readline().split()
    vals_C[jcase] = float(seg[0])
    vals_F[jcase] = float(seg[1])
    vals_X[jcase] = float(seg[2])
infile.close()


outfile=open(fname_output, 'w')
for jcase in range(numcase):
    print 'jcase=%i / numcase=%i'%(jcase, numcase)
    answer = solve_case(vals_C[jcase], vals_F[jcase], vals_X[jcase])
    outfile.write('Case #%i: %.7f\n'%(jcase+1, answer))
outfile.close()


print '*********************'
print ' Normal End :)       '
print '*********************'
