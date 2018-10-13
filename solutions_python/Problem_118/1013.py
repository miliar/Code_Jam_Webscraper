#!/usr/bin/env python
import sys
import numpy as np
import time
def fair(x):
    strx = list(str(x))
    length = (int)(len(strx)/2.)
    for i in range(length):
        if(not strx[i]==strx[-(i+1)]):
            return False
    return True
def judge(case):
    squreroot = np.sqrt(case)
    round = squreroot.astype(int)
    index = (squreroot-round)==0
    newcase = case[index]
    newsqreroot = round[index]
    count = 0
    for i in range(len(newcase)):
        if(fair(newcase[i]) and fair(newsqreroot[i])):
            count+=1
    return count

def main():
    infile = sys.argv[1]
    fin=open(infile,mode='r')
    nT = int(fin.readline().rstrip())
    for i in xrange(nT):
        string=fin.readline().rstrip().split()
        #print string
        case=np.array(range(int(string[0]),int(string[1])+1))
        #print case,case[0],case[-1]
        result=judge(case)
        print 'Case #%d: %d' % (i+1,result)
    fin.close()
    return

if __name__=='__main__':
    main()
