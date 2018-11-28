from __future__ import division

import os
import os.path, time
import itertools


fo=open("A-large.in")
fw=open("A-large.txt","w")
'''fo=open("test.txt")
fw=open("testout.txt","w")'''
n=int(fo.readline())
for k in range(0,n):
        Mush=[]
        Dif=[]
        num=int(fo.readline())
        Mushs=fo.readline().split()
        Eat1=0
        Eat2=0
        Eat3=0
        for i in range(0,len(Mushs)):
                Mush.append(int(Mushs[i]))
        for i in range(0,len(Mush)-1):
                if Mush[i+1]<Mush[i]:
                        Eat1=Eat1+Mush[i]-Mush[i+1]
                Dif.append(Mush[i+1]-Mush[i])
        Rate=-min(Dif)/10
        for i in range(0,len(Mush)-1):
                Eat2=Eat2+min(Mush[i],Rate*10)
        fw.write("Case #"+ str(k+1)+": ")       
        fw.write(str(Eat1)+" " +str(int(Eat2))+ "\n")         
fw.close()        
        
                





