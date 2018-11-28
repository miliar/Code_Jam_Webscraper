import sys
import fileinput
import math
MaxCaseNum=0
CaseNum=0.0
Diners=0
InStr=''
SplitStr=[]

def returnLowestPrime(int_in):
    for n in range(3, int(math.sqrt(int_in))+1, 2):
        if (int_in % n) == 0:
            return n
    return 1

def castSplitSort(str_input):
    str_split=str_input.rsplit(" ")
    str_splitConv=[]
    for plate in range(0,Diners):
        str_splitConv.append(int(str_split[plate]))
        str_splitConv.sort(reverse=True)
    return str_splitConv

def divPrimeFork(str_split, int_prime):
    numlist_splitStr=list(str_split)
    for x in range(0, int_prime):
        numlist_splitStr.append((numlist_splitStr[0]/int_prime)+0)
    numlist_splitStr.pop(0)
    numlist_splitStr.sort(reverse=True)
    #print numlist_splitStr
    return findLowest(numlist_splitStr)

  

def findLowest(numlist_splitStr):
    minTime=numlist_splitStr[0]
    worstCase=minTime
    lowPrime=0
    
    for iter in range(0,minTime):

        if(iter+numlist_splitStr[0])<minTime:
            minTime=iter+numlist_splitStr[0]

        #print " minTime %d, iter %d, runTime %d, spStr %s" % (minTime, iter, iter+numlist_splitStr[0],numlist_splitStr)
        if((numlist_splitStr[0]%2)==0): #if even
            numlist_splitStr.append(numlist_splitStr[0]/2)
            numlist_splitStr.append(numlist_splitStr[0]/2)
            numlist_splitStr.pop(0)
            numlist_splitStr.sort(reverse=True)
        else:
            lowPrime=returnLowestPrime(numlist_splitStr[0])
            if lowPrime!=1:
                #print " Checking %d" % (lowPrime)
                lowPrime += divPrimeFork(numlist_splitStr, lowPrime)+iter+(-1)
                if lowPrime < minTime:
                    #print " found to be lower"
                    minTime = lowPrime
            
            numlist_splitStr.append((numlist_splitStr[0]/2)+0)
            numlist_splitStr.append((numlist_splitStr[0]/2)+1)
            numlist_splitStr.pop(0)
            numlist_splitStr.sort(reverse=True)
    
    return minTime

for line in fileinput.input():

    if MaxCaseNum==0:
        MaxCaseNum=int(line)
        continue
    CaseNum+=.5
    if(CaseNum%1 == .5):
        Diners=int(line)
    else:
        InStr=str(line)
        SplitStr=castSplitSort(InStr)
        #print " Init Case #%d:initDiners%d"%(int(CaseNum),Diners)
        print "Case #%d: %d" % (int(CaseNum), findLowest(SplitStr))

        
        
