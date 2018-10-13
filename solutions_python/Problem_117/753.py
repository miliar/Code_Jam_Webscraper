#!/usr/bin/env python
import sys
import numpy as np
import time

def judge(case,a):
    indexs=np.where(case<a)
    if(len(indexs[0])==0):
        return 0
    elif(len(indexs[0])==1):
        flagx=(case[indexs[0],:]<a).all()
        flagy=(case[:,indexs[1]]<a).all()
        if(not (flagx or flagy)):
            return 1
        else:
            return 0
    else:
        for i in xrange(len(indexs[0])):
            try:
                flagx=(case[indexs[0][i],:]<a).all()
                flagy=(case[:,indexs[1][i]]<a).all()
            except IndexError:
                print case
                print indexs,len(indexs),len(indexs[0]),indexs[0][i]
                print case[:,2]
                raise

            if(not (flagx or flagy)):
                return 1
        return 0

def parse(string,flag):
    if(flag):
        return [paradicX[x] for x in list(string)]
    else:
        return [paradicO[x] for x in list(string)]
def main():
    infile = sys.argv[1]
    status = ['YES','NO']
    fin=open(infile,mode='r')
    nT = int(fin.readline().rstrip())
    for i in xrange(nT):
        size=fin.readline().rstrip().split() 
        case=[]
        for l in xrange(int(size[0])):
            data=fin.readline().rstrip().split()
            case+=data
        case=np.array(case,dtype=int)
        a = max(max(case),2)
        
        case=case.reshape((int(size[0]),int(size[1])))
        for h in xrange(a-1):
            result=judge(case,a-h)
            if(result==1):
                break
        print 'Case #%d: %s' % (i+1,status[result])
        #print case
    fin.close()
    return

if __name__=='__main__':
    main()
