#!/usr/bin/python
import sys
import os
def switchF(QList,SEList,cSE,cQ,nS,c):     
     nS+=1
     i=0
     maxSE=100000000000
     maxK=-1
     valK=cQ
     while i<len(SEList):
        if i!=cSE:
            k=cQ
            while k<len(QList):
                if SEList[i]==QList[k]:
                  break;
                k+=1
            if maxK<k-cQ:
                   maxK=k-cQ
                   maxSE=i
                   valK=k                   
        i+=1
     if valK==len(QList):
         print  "Case #"+str(c+1)+": "+str(nS)
     else:         
         switchF(QList,SEList,maxSE,valK,nS,c)


#--Read input file----
inFile=sys.argv[1]

inId=open(inFile,"r")


#---Read No. of Cases----
theData=inId.readline()
theData=theData[:len(theData)-1]
noCases=int(theData)
i=0
while i<noCases:
   #---Read No. of SE---
   theData=inId.readline()
   theData=theData[:len(theData)-1]
   #print "SE "+theData
   noSE=int(theData)
   j=0
   SEList=[]
   while j<noSE:
        theData=inId.readline()
        theData=theData[:len(theData)-1]      
        #print theData        
        SEList.append(theData)
        j+=1
   #--- Read No. of Query---
   theData=inId.readline()
   theData=theData[:len(theData)-1]
   noQ=int(theData)
   #print "Q "+theData
   QList=[]
   k=0
   while k<noQ:
        theData=inId.readline()
        theData=theData[:len(theData)-1] 
        QList.append(theData) 
        k+=1
   #print QList
   #------Select minimum-------
   st=0
   maxSE=100000000
   maxK=-1
   
   while st<noSE:
     k=0
     while k<len(QList):
        if SEList[st]==QList[k]:
            break;
        k+=1
     if maxK<k:
        maxK=k
        maxSE=st
     st+=1

   if maxK==len(QList):
         print  "Case #"+str(i+1)+": 0"
   else:
         #print "Case "+str(c)+": "+str(maxSE)+" "+str(valK)
         switchF(QList,SEList,maxSE,maxK,0,i)            
   i+=1



