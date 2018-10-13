from __future__ import division

import os
import os.path, time
import itertools


fo=open("B-large.in")
fw=open("B-large.out","w")
n=int(fo.readline())
for k in range(0,n):
        HW=fo.readline().split()
        C=float(HW[0])
        F=float(HW[1])
        X=float(HW[2])
        print "Case #"+ str(k+1)+": "
        fw.write("Case #"+ str(k+1)+": ")
        Total1=X/2
        n=0
        while True:
                Total2=Total1-X/(2+n*F)+C/(2+n*F)+X/(2+(n+1)*F)
                if Total1<Total2:
                        break
                n=n+1
                Total1=Total2
        fw.write(format(Total1, '.7f')+"\n")
fw.close()        
        
                





