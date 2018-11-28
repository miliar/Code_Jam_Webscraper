from __future__ import division

import os
import os.path, time
import itertools
import numpy as np
import copy
def trypack(anspeed):
        sp=min(anspeed)

                
        return sp
        

        


#fo=open("test.txt")
#fw=open("test_out.txt","w")
#fo=open("A-small-attempt0.in")
#fw=open("A-small-attempt0.out","w")
fo=open("A-large.in")
fw=open("A-large.out","w")

n=int(fo.readline())
for k in range(0,n):
        
        print "Case #"+ str(k+1)+": "
        D,N=fo.readline().rstrip().split()
        N=int(N)
        D=int(D)
        horses=[]
        speeds=[]
        timeleft=[]
        anspeed=[]
        for i in range(0,N):
                K,S=fo.readline().rstrip().split()
                K=int(K)
                S=int(S)
                horses.append(K)
                speeds.append(S)
                timeleft.append((D-K)/S)
                anspeed.append(D/((D-K)/S))
                

        sp=min(anspeed)
    
                
                
        

       
        fw.write("Case #"+ str(k+1)+": ")
        fw.write(str(sp)+"\n")         
fw.close()        
        
                





