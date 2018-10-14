#!/usr/bin/python
#
# This code was written by Norio TAKEMOTO 2014-4-11.

import numpy as np


###################################
fname_input="A-small-attempt0.in"
fname_output="output_problemA.dat"
numgrid=2
numrow=4
numcol=4
###################################



def solve_case(case_irows, case_grids):
    set_first = set(case_grids[0][case_irows[0]][:])
    set_second = set(case_grids[1][case_irows[1]][:])
    intersection_first_second = set_first.intersection(set_second)

    if 1==len(intersection_first_second):
        for elm in intersection_first_second:
            s_answer = str(elm)
    elif 0==len(intersection_first_second):
        s_answer = "Volunteer cheated!"
    else:
        s_answer = "Bad magician!"
    return s_answer


infile=open(fname_input, 'r')
numcase = int(infile.readline())
answers=np.empty((numcase,numgrid),dtype=int)
grids  =np.empty((numcase,numgrid,numrow,numcol),dtype=int)
for jcase in range(numcase):
    for jgrid in range(numgrid):
        answers[jcase][jgrid] =  int(infile.readline())
        for jrow in range(numrow):
            seg = infile.readline().split()
            for jcol in range(numcol):
                grids[jcase][jgrid][jrow][jcol] = int(seg[jcol])
infile.close()

irows = answers-1

outfile=open(fname_output, 'w')
for jcase in range(numcase):
    print 'jcase=%i / numcase=%i'%(jcase, numcase)
    s_answer= solve_case(irows[jcase][:], grids[jcase][:][:][:])
    outfile.write('Case #%i: %s\n'%(jcase+1, s_answer))
outfile.close()


print '*********************'
print ' Normal End :)       '
print '*********************'
