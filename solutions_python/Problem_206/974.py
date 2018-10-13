#!/usr/bin/python3
#
# This script was written by Norio TAKMEOTO 2017-04-15-05:38

import numpy as np


###
#inputfname='input_ex.dat'
#outputfname='output_ex.dat'
#inputfname='A-small-attempt0.in'
#outputfname='output_s.dat'
inputfname='A-large.in'
outputfname='output_l.dat'
##



def solve(destD, posK, speedS):

    #numhorseN = np.size(posK)
    #assert numhorseN == np.size(speedS)

    timeT = (destD-posK)/speedS
    #max_timeT = np.max(timeT)
    #print('max_timeT=%10f'%(max_timeT))
    #speed_cruise = destD/max_timeT

    #return speed_cruise 
    return destD/ np.max(timeT)


fin = open(inputfname, 'r')
fout = open(outputfname, 'w')

line=fin.readline()
numcases = int(line)
for jcase in range(numcases):
    print('-----')
    print('jcase=',jcase)
    line=fin.readline()
    ss = line.split()
    destD    = float(ss[0])
    numhorseN=   int(ss[1])
    posK   = np.empty((numhorseN,))
    speedS = np.empty((numhorseN,))
    for jhorse in range(numhorseN):
        line=fin.readline()
        ss = line.split()
        posK[jhorse]=float(ss[0])
        speedS[jhorse]=float(ss[1])
    speed_cruise = solve(destD, posK, speedS)
    fout.write('Case #%i: %24.14e\n'%(jcase+1, speed_cruise))
    

fin.close()
fout.close()
    
print('normal end')
