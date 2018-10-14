#!/usr/bin/python3
#
# This script was written by Norio TAKMEOTO 2017-04-08-02:41

import numpy as np

###
#inputfname='inputA_ex.dat'
#outputfname='outputA_ex.dat'
#inputfname='A-small-attempt0.in'
#outputfname='outputA_samll.dat'
inputfname='A-large.in'
outputfname='outputA_large.dat'
###


def solve(state, kflipper):

    #print('state: ', state)
    #print('kflipper=', kflipper)

    nflip=0
    ns = np.size(state)
    for jst in range(ns-kflipper+1):
        if not state[jst]:
            state[jst:jst+kflipper] = np.logical_not( state[jst:jst+kflipper] )
            nflip +=1
        #print('jst=',jst)
        #print('state: ', state)
    if not np.all(state[ns-kflipper+1:ns]):
        return None
    else:
        return nflip


fin = open(inputfname, 'r')
fout = open(outputfname, 'w')

line=fin.readline()
numcases = int(line)
jcase=0
for line in fin:
    segs = line.split()
    state = np.array([segs[0][js]=='+' for js in range(len(segs[0]))], dtype=bool)
    kflipper = int(segs[1])

    #print('-----')
    #print('jcase=',jcase)
    nflip = solve(state, kflipper)
    if nflip==None:
        fout.write('Case #%i: IMPOSSIBLE\n'%(jcase+1))
    else:
        fout.write('Case #%i: %i\n'%(jcase+1,nflip))
    jcase+=1
    

fin.close()
fout.close()
    

