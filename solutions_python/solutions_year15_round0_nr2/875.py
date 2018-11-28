#!/usr/bin/env python
import numpy as np
import scipy as sp
import os
import sys

def Decide(maxD,Darr):
    
    maxreduce = 1
    
    count = 0
    for i in xrange(2,(int)(maxD/2)+1): 
        reduced = i
        #maxreduce = min(Darr[-1]-Darr[-2],reduced)
        #newmaxD = max(Darr[-2],Darr[-1]-(int)(Darr[-1]/2))
        nmax = len(np.where(Darr==maxD)[0])
        singlesplit = get_result(maxD,np.array([maxD]))
        if nmax>=singlesplit:
            count=0
            break
        tempDarr = np.delete(Darr,np.where(Darr==maxD)[0][0])
        newarr = np.array(list(tempDarr)+[reduced,maxD-reduced])
        newmaxD = max(newarr)
        timereduce =maxD-get_result(newmaxD,newarr)
        #print i,timereduce
        if timereduce>maxreduce:
            maxreduce = timereduce
            count=i
            newarrsave = newarr
    if count==0:
    #if maxreduce<=1:
        #eat
        return [maxD-1,Darr-1]
    else:
        #move
        return [max(newarrsave),newarrsave]

def get_result(D,Darr):
    #print "start",D,Darr
    maxD = max(Darr)
       
    result=0
    if len(Darr)==1:
        smalltimearr=np.array([1,2,3,3,4,4,5,5,5])
        return smalltimearr[maxD-1] 
    while (maxD>3):
        maxD,Darr = Decide(maxD,Darr)
        #print maxD,Darr
        result+=1
        #if(result>5):
        #    break
    if maxD==1:
        return result+1
    if maxD==2:
        return result+2
    if maxD==3:
        return result+3
     
    return result


def main(infile):
    fin=open(infile,mode='r')
    fout = open("test_output.txt",mode='w')
    ncase = int(fin.readline())
    for i in xrange(ncase):
        #print i
        D = int(fin.readline())
        Darr = np.array(fin.readline().split()).astype(int)
        result = get_result(D,np.sort(Darr))
        fout.write("Case #%d: %d\n" % ((i+1),result))
    fin.close()
    fout.close()
    return
if __name__=='__main__':
    main(sys.argv[1])
