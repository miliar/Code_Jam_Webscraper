'''
Created on Apr 13, 2013

@author: FENNERK
'''
from numpy import *

input=open('A-large.in','r')
output=open('large_output.txt','w')

cases=input.readline()

grid=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
grid2=[[1,5,9,13],[2,6,10,14],[3,7,11,15],[4,8,12,16]]

diag1=[1,6,11,16]
diag2=[4,7,10,13]

for j in range(0,int(cases)):
    line=[]
    Os=[]
    Xs=[]
    done=-1

    for i in range(0,4):
        line=input.readline().strip()
       
        for k in range(0,4):
            if line[k]=='O':
                Os.append(i*4+k+1)
            if line[k]=='X':
                Xs.append(i*4+k+1)
            if line[k]=='T':
                Os.append(i*4+k+1)
                Xs.append(i*4+k+1)
            if line[k]=='.':
                done=0

    input.readline()
        
    for m in range(0,4):
        r=[row[m] for row in grid]
        c=[row[m] for row in grid2]
        
        
        if set(r).issubset(Os):
            done=1
                    
        if set(c).issubset(Os):
            done=1
                        
        if set(diag1).issubset(Os):
            done=1
            
        if set(diag2).issubset(Os):
            done=1
        
        if set(r).issubset(Xs):
            done=2
        
        if set(c).issubset(Xs):
            done=2
            
        if set(diag1).issubset(Xs):
            done=2
            
        if set(diag2).issubset(Xs):
            done=2
    
    if done==-1:
        output.write("Case #" + str(j+1) + ": Draw\n")
    elif done==0:
        output.write("Case #" + str(j+1) + ": Game has not completed\n")
    elif done==1:
        output.write("Case #" + str(j+1) + ": O won\n")
    else:
        output.write("Case #" + str(j+1) + ": X won\n")
        
    
