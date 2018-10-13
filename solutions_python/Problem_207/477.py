import math
import numpy as np

fout = open('C:\\Users\\Soheil\\Documents\\Visual Studio 2017\\Projects\\B\\B\\Boutput-small.out', 'w')
#fout = open('C:\\Users\\Soheil\\Documents\\Visual Studio 2017\\Projects\\B\\B\\Boutput-large.out', 'w')


T=int(input())
for t in range(1,T+1):
    print(t)
    N, R, O, Y, G, B,V=map(int, input().split())
    unicorns=[]
    for i in range(0,R):
        unicorns.append('R')
    for i in range(0,B):
        unicorns.append('B')
    for i in range(0,Y):
        unicorns.append('Y')
    for i in range(0,O):
        unicorns.append('O')
    for i in range(0,G):
        unicorns.append('G')
    for i in range(0,V):
        unicorns.append('V')
    #print(unicorns)
    unicornList=[]
    unicornList.append(unicorns[0])
    impossibleflag=False
    lastElement=[]
    if(unicornList[0]=='R'):
        R=R-1
        lastElement=['Y','B','G']
    elif(unicornList[0]=='B'):
        B=B-1
        lastElement=['R','Y','O']
    elif(unicornList[0]=='Y'):
        Y=Y-1
        lastElement=['B','R','V']
    else:
        impossibleflag=True
   
    for i in range(1,N):
        currentColor=unicornList[len(unicornList)-1]
        if(currentColor=='R'):
            if(G>0):
                G=G-1
                unicornList.append('G')
            elif(Y>B and Y>0):
                Y=Y-1
                unicornList.append('Y')
            elif(B>0):
                B=B-1
                unicornList.append('B')
            else:
                impossibleflag=True
                break;
        if(currentColor=='B'):
            if(O>0):
                O=O-1
                unicornList.append('O')
            elif(Y>R and Y>0):
                Y=Y-1
                unicornList.append('Y')
            elif(R>0):
                R=R-1
                unicornList.append('R')
            else:
                impossibleflag=True
        if(currentColor=='Y'):
            if(V>0):
                V=V-1
                unicornList.append('V')
            elif(B>R and B>0):
                B=B-1
                unicornList.append('B')
            elif(R>0):
                R=R-1
                unicornList.append('R')
            else:
                impossibleflag=True        
        if(currentColor=='O'):
            if(B>0):
                B=B-1
                unicornList.append('B')
            else:
                impossibleflag=True 
        if(currentColor=='G'):
            if(R>0):
                R=R-1
                unicornList.append('R')
            else:
                impossibleflag=True 
        if(currentColor=='V'):
            if(Y>0):
                Y=Y-1
                unicornList.append('Y')
            else:
                impossibleflag=True 
    if(any(unicornList[len(unicornList)-1]==x for x in lastElement) and impossibleflag==False):
        fout.write("Case #{}: {}\n".format(t,''.join(unicornList)))
        #print(t,''.join(unicornList))
    else:
        #print(t,"IMPOSSIBLE")
        fout.write("Case #{}: {}\n".format(t,"IMPOSSIBLE"))

fout.close()