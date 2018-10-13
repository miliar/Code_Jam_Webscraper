#!/usr/bin/env python
import sys
import numpy as np
import time
def loadcases(r):
    a = np.arange(40)
    area = (2*r+1)*(a+1)+4*a*(a+1)/2.
    return area
def judge(case):
    r = int(case[0])
    t = int(case[1])
    
    a = np.arange(40)
    answer=loadcases(r)
    #print answer,t 
    return max(a[answer<=t])+1


def main():
    infile = sys.argv[1]
    fin=open(infile,mode='r')
    nT = int(fin.readline().rstrip())
    for i in xrange(nT):
        string=fin.readline().rstrip()
        case=string.split()
        result=judge(case)
        print 'Case #%d: %d' % (i+1,result)
    fin.close()
    return

if __name__=='__main__':
    main()
