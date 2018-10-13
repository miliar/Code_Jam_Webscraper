'''
Created on Apr 13, 2013

@author: akshay
'''
fp = open("B-large.in","r")
list=fp.readlines()
list=[x.strip() for x in list]
list=[x.split() for x in list]
for i in range(len(list)):
    list[i] = [int(x) for x in list[i]]

T=int(list.pop(0)[0])

i=0
caseNo=1
while i<len(list):
    N=list[i][0]
    M=list[i][1]
    NXM=[]
    check=0
    for j in range(1,N+1):
        NXM.append(list[i+j])
    
    for n in range(N):
        for m in range(M):
            column=[]
            row=NXM[n]
            checkRow=0
            checkCol=0
            for x in NXM:
#                column.append(x[m])
                if NXM[n][m]<x[m]:
                    checkCol+=1
#                    print checkCol,x,NXM,NXM[n][m],x[m],n,m
                    break
            for x in row:
#                print x,NXM
                if NXM[n][m]<x:
                    checkRow+=1
                    break
            if checkRow!=0 and checkCol!=0:
                check+=1
                
                break
        if check>0:
            print "Case #%d: NO"%(caseNo)
            break
    if check==0:
        print "Case #%d: YES"%(caseNo)
    caseNo+=1        
    i+=N+1