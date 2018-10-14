from __future__ import division

import os
import os.path, time
import itertools


fo=open("D-small-attempt1.in")
fw=open("D-small-attempt1.out","w")
#fo=open("test.txt")
#fw=open("text_out.txt","w")
n=int(fo.readline())
for k in range(0,n):
        text=fo.readline()
        Line=[int(n) for n in text.split()]
        print Line
        X=Line[0]
        R=Line[1]
        C=Line[2]
        Win="RICHARD"
        if (C*R//X==C*R/X) and (X!=4):
                Win="GABRIEL"
        if X==4 and (C*R==16 or C*R==12) :
                Win="GABRIEL"
        if X==3 and (C*R==3) :
                Win="RICHARD"
        print Win
        fw.write("Case #"+ str(k+1)+": ")
        fw.write(str(Win)+"\n")         
fw.close()        
        
                





