from __future__ import division

import os
import os.path, time
import itertools
def sign(c):
        if c>0:
                return 1
        if c<0:
                return -1
        
def mult(a,b):
        c=sign(a*b)
        a=abs(a)
        b=abs(b)
        if a==1 or b==1:
                return c*a*b
        elif a==2:
                if b==2:
                        return -1*c
                if b==3:
                        return 4*c
                if b==4:
                        return -3*c
        elif a==3:
                if b==2:
                        return -4*c
                if b==3:
                        return -1*c
                if b==4:
                        return 2*c
        elif a==4:
                if b==2:
                        return 3*c
                if b==3:
                        return -2*c
                if b==4:
                        return -1*c
                
'''
def sort(ST):
        for i in range(1,len(ST)):
                for j in range(1,len(ST)-1):
                        if ST[j+1]<ST[j]:
                                a=ST[j]
                                ST[j]=ST[j+1]
                                ST[0]=ST[0]*-1
                                ST[j+1]=a
        return ST'''

fo=open("C-small-attempt1.in")
fw=open("C-small-attempt1.out","w")
#fo=open("test.txt")
#fw=open("test_out.txt","w")
n=int(fo.readline())
for k in range(0,n):
        print "Case #"+ str(k+1)+": "
        HW=fo.readline().split()
        Mult=int(HW[1])
        ST=fo.readline().strip('\n')*Mult
        NewSt=[]
        for i in range(0,len(ST)):
                if ST[i]=="i":
                        NewSt.append(2)
                elif ST[i]=="j":
                        NewSt.append(3)
                elif ST[i]=="k":
                        NewSt.append(4)
        #print NewSt
        while len(NewSt)>=3 and (NewSt[0]!=2):
                a=NewSt[0]
                NewSt[1]=mult(a,NewSt[1])
                NewSt.pop(0)
        
        while len(NewSt)>=3 and (NewSt[1]!=3):
                a=NewSt[1]
                NewSt[2]=mult(a,NewSt[2])
                NewSt.pop(1)
        
        while len(NewSt)>=3 and (NewSt[2]!=4):
                a=NewSt[2]
                NewSt[3]=mult(a,NewSt[3])
                NewSt.pop(2)
        while len(NewSt)>=5:
                a=NewSt[3]
                NewSt[4]=mult(a,NewSt[4])
                NewSt.pop(3)
        #print NewSt
        if NewSt==[2,3,4] or NewSt==[2,3,4,1]:
                Answer="YES"
        else:
                Answer="NO"
        #print Answer
                
                
                
                
                
                 
                       
        
        
        fw.write("Case #"+ str(k+1)+": ")
        fw.write(str(Answer)+"\n")         
fw.close()        
        
                





