#!/usr/bin/python3
#
# This script was written by Norio TAKMEOTO 2017-04-08-04:16.

import numpy as np


###
#inputfname='input_ex.dat'
#outputfname='output_ex.dat'
inputfname='C-small-1-attempt0.in'
outputfname='output_samll_1.dat'
#inputfname='C-large.in'
#outputfname='output_large.dat'
###


def partial(status):
    '''
    status[jvac,0]: stool index of the jvac-th vacant segment
    status[jvac,1]: number of vacant stools in jvac-th segment
    '''

    numvseg=status.shape[0]
    jmax = np.argmax(status, axis=0)[1]
    # .. In case of multiple occurrences of the maximum values, 
    # the indices corresponding to the first occurrence are returned.
    #print('jmax=', jmax)
    #print('status=', status)
    
    newstatus = np.empty((numvseg+1,2), dtype=int)
    #print('newstatus.shape=', newstatus.shape)
    if jmax>0:
        newstatus[0:jmax,:] = status[0:jmax,:]
    nvac = status[jmax,1]
    nnvl = (nvac-1)//2
    nnvr = nvac-nnvl-1
    assert nnvl<=nnvr
    jj=jmax
    if nnvl>0:
        newstatus[jj,0]   = status[jmax,0]
        newstatus[jj,1]   = nnvl
        jj+=1
    if nnvr>0:
        newstatus[jj,0] = status[jmax,0]+nnvl+1
        newstatus[jj,1] = nnvr
        jj+=1
    jend = jj+(numvseg-(jmax+1))
    newstatus[jj:jend,:] = status[jmax+1:numvseg,:]

    return (newstatus[0:jend], nnvl, nnvr)


def solve(nstool, kpeople):

    status = np.array([[0,nstool]])
    for jpeople in range(kpeople):
        status, minlr,maxlr = partial(status)

    return maxlr, minlr


fin = open(inputfname, 'r')
fout = open(outputfname, 'w')

line=fin.readline()
numcases = int(line)
jcase=0
for line in fin:
    seg=line.split()
    nstool = int(seg[0])
    kpeople= int(seg[1])
    #print('-----')
    #print('jcase=',jcase)
    (maxlr, minlr) = solve(nstool, kpeople)
    fout.write('Case #%i: %i %i\n'%(jcase+1,maxlr,minlr))
    jcase+=1
    

fin.close()
fout.close()
    

