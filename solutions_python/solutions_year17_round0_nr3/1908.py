import string
import sys
import numpy as np
import math as ma

output=[]
def mainFunc():
    f=open("C-small-1-attempt0.in","r")
    x=f.read()
    y=x.split()
    T=int(y[0]); del(y[0]);j=0
    for i in range(T):
        Ns= int(y[j]); Np= int(y[j+1]);j +=2
        x=[0]*(Ns+2)#status of stalls
        x[0]=1;x[Ns+1]=1
        for ppl in range(Np):
            offset=1; count=[]; indexarr=[]; check=0;output=[]
            while check>=0:
                temp=x[x.index(0,offset):]
                count.append(temp.index(1))
                indexarr.append(x.index(0,offset))
                offset= x.index(1,offset+1)
                try:
                    x.index(0,offset)
                except:
                    check=-1
            #print indexarr[count.index(max(count))]
            indexOfMax=indexarr[count.index(max(count))]
            #print count, indexarr
            indexOfMax= indexOfMax+int(ma.ceil(float(max(count))/2))-1
            output.append(x.index(1,indexOfMax+1)-indexOfMax-1)
            temp1=x[:];temp1.reverse()
            output.append(temp1.index(1,len(temp1)-indexOfMax)-(len(temp1)-indexOfMax))
            x[indexOfMax]=1
            #print offset,count,indexarr,indexOfMax,x
        print ("Case #%d: %d %d"%(i+1,max(output),min(output)))
mainFunc()