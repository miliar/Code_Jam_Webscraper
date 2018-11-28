import string
import sys
import numpy as np

output=[]
def mainFunc():
    f=open("A-large.in","r")
    x=f.read()
    y=x.split()
    T=y[0]; del(y[0]);i=0; outputCount=0
    while outputCount<int(T):
        count=0
        k=int(y[i+1]); s=y[i]
        s=list(s); j=0
        while j< len(s)-k+1:
            if s[j]=="-":
                count +=1
                for x in range(k):
                    s[j+x]=change(s[j+x])
            j +=1
        s="".join(s)
        if s.find("-")>0:
            outputCount +=1
            print ("Case #%d: IMPOSSIBLE"%outputCount)
        else:
            outputCount +=1    
            print ("Case #%d: %d"%(outputCount,count))
        i +=2
def change(a):
    if a=="+":
        return "-"
    else:
        return "+"

mainFunc()