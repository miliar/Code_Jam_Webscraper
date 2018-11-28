import os
import re

filein=open("c:\\codejam\\alien\\A-large.in",'r')
fileout=open("c:\\codejam\\alien\\A-large.out",'w')

s=filein.readline().replace('\n','').split(' ')
L=int(s[0])
D=int(s[1])
N=int(s[2])
a=[]

for i in range(D):
    a.append(filein.readline().replace('\n',''))
for i in range(N):
    final=0
    s=filein.readline().replace('\n','')
    s=s.replace('(','[').replace(')',']')
    
    r=re.compile(s)
    for j in a:
        if r.match(j):
            final+=1       
    fileout.write("Case #"+str(i+1)+": "+str(final)+'\n')      
        
           
        
        
filein.close()
fileout.close()