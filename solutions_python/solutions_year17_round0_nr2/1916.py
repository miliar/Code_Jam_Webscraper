#!/usr/bin/python3
#
# This script was written by Norio TAKMEOTO 2017-04-08-04:16.

import numpy as np


###
#inputfname='input_ex.dat'
#outputfname='output_ex.dat'
#inputfname='B-small-attempt0.in'
#outputfname='output_samll.dat'
inputfname='B-large.in'
outputfname='output_large.dat'
###



def solve(inum):
   
    digits=np.array([int(cc) for cc in str(inum)])
    #print('digits=', digits)
    for jj in range(len(digits)-1):
        if digits[jj] > digits[jj+1]:
            jst=jj
            while jst>0 and digits[jst]==digits[jst-1]:
                jst -=1
            digits[jst] -= 1 
            digits[jst+1:] = 9
            break

    return int(''.join([str(dd) for dd in digits]))


fin = open(inputfname, 'r')
fout = open(outputfname, 'w')

line=fin.readline()
numcases = int(line)
jcase=0
for line in fin:
    inum = int(line)
    #print('-----')
    #print('jcase=',jcase)
    #print('inum=',inum)
    ians = solve(inum)
    fout.write('Case #%i: %i\n'%(jcase+1,ians))
    jcase+=1
    

fin.close()
fout.close()
    

