from __future__ import division

import os
import os.path, time
import itertools


fo=open("A-large.in")
fw=open("A-large.out","w")
n=int(fo.readline())
for k in range(0,n):
        Shy=[]
        HW=fo.readline().split()
        MS=int(HW[0])
        ST=HW[1]
        for i in range(0,MS+1):
                Shy.append(int(ST[i]))
        print "Case #"+ str(k+1)+": "
        fw.write("Case #"+ str(k+1)+": ")
        print Shy
        Standing=0;
        Guests=0;
        for i in range(0,MS+1):
                while i>Standing:
                                Guests=Guests+1;
                                Standing=Standing+1;
                if i<=Standing:
                        Standing=Standing+Shy[i]
        fw.write(str(Guests)+"\n")         
fw.close()        
        
                





