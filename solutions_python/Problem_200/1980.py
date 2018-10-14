import string
import sys
import numpy as np

output=[]
def mainFunc():
    f=open("B-large.in","r")
    x=f.read()
    y=x.split()
    T=int(y[0]); del(y[0]);
    for i in range(T):
        N=int(y[i])
        if N<10**9:
            N=findNeo(N)
            print("Case #%d: %d"%(i+1, int(N)))
        else:
            N=list(str(N));j=0
            while j<len(N)-1:
                if N[len(N)-j-1]<N[len(N)-j-2]:
                    N=np.array(N)
                    N[len(N)-j-1:]="9"
                    N[len(N)-j-2]=str(int(N[len(N)-j-2])-1)
                j +=1
            print("Case #%d: %s"%(i+1, str(int("".join(N)))))

"""   
            N=(int(y[i]))%(10**9)
            if(N==0):
                N=int(y[i])-1
            else:
                N1=findNeo(N)
                N=str(int(y[i])/(10**9))+"0"*(len(N)-len(N1))+str(N1)
while N!=int("".join(sorted(str(N)))):
                N -=1
            print("Case #%d: %d"%(i+1, N))
"""
def findNeo(N):
    N=list(str(N))
    while N!=sorted(N):
        N=list(str(int("".join(N))-1))
    return int("".join(N))
mainFunc()

