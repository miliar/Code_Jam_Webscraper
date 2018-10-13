#!/usr/bin/env python
import sys
import numpy as np
import time
key = ['X','O','T','.']
valueX = [1,-1,1,0]
valueO = [1,-1,-1,0]
paradicX = dict(zip(key,valueX))
paradicO = dict(zip(key,valueO))

def judge(case):
    case=np.array(case).reshape(4,4)
    meana=case.sum(0)
    if (meana==4).any():
        return 0
    elif (meana==-4).any():
        return 1
    else:
        meanb=case.sum(1)
        if(meanb==4).any():
            return 0
        elif(meanb==-4).any():
            return 1
        else:
            sum1=0;sum2=0
            for i in xrange(4):
                sum1 += case[i,i]
                sum2 += case[3-i,i]
            if(sum1==4 or sum2==4):
                return 0
            elif(sum1==-4 or sum2==-4):
                return 1
            else:
                if(not (case==0).any()):
                    return 2
                else:
                    return 3

def parse(string,flag):
    if(flag):
        return [paradicX[x] for x in list(string)]
    else:
        return [paradicO[x] for x in list(string)]
def main():
    infile = sys.argv[1]
    status = ['X won','O won','Draw','Game has not completed']
    fin=open(infile,mode='r')
    nT = int(fin.readline().rstrip())
    for i in xrange(nT):
        case=[]
        for l in xrange(4):
            string=fin.readline().rstrip()
            case+=string
        ncase=parse(case,True)
        result=judge(ncase)
        if(result==3):
            ncase=parse(case,False)
            result=judge(ncase)
        print 'Case #%d: %s' % (i+1,status[result])
        fin.readline()
    fin.close()
    return

if __name__=='__main__':
    main()
