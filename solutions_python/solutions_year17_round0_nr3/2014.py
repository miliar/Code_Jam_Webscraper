'''
Created on 8 avr. 2017

@author: Regis DUPUIS
'''
from math import ceil

def getBestIndex(stalls, first=False):
    if(first):
        nbOfStalls = len(stalls)
        return ceil(nbOfStalls/2) - 1
    else:
        RsMax = 0
        LsMax = 0
        idxMax = -1
        firstEqual = False
        
        for i in range(1, len(stalls)-1):
            if stalls[i] == False :
                Rs = computeRs(stalls, i)
                Ls = computeLs(stalls, i)
                if(min(Rs, Ls) > min(RsMax, LsMax)
                   or ( min(Rs, Ls) == min(RsMax, LsMax) and max(Rs, Ls) > max(RsMax, LsMax) )):
                    RsMax=Rs
                    LsMax=Ls
                    idxMax=i
#                 elif(firstEqual==False and min(Rs, Ls) == min(RsMax, LsMax)):
#                     firstEqual = True
#                     RsMax=Rs
#                     LsMax=Ls
#                     idxMax=i
    
        return idxMax
    
def getMinMax():
    pass

def computeLs(stalls, idx):
    Ls = 0
    idx -= 1
    while(idx>0 and stalls[idx]==False):
        Ls += 1
        idx -= 1
    return Ls

def computeRs(stalls, idx):
    Rs = 0
    idx += 1
    while(idx<len(stalls)-1 and stalls[idx]==False):
        Rs += 1
        idx += 1
    return Rs

def fillStallWithOnePerson(stalls, first=False):
    idx = getBestIndex(stalls, first)
    stalls[idx]=True

    return idx
    
def fillStallWithKPerson(n, k):
    if n == k :
        return 0, 0
    
    stalls = initStalls(n)
    
    for person in range(0, k):
        if person == 0:
            idx = fillStallWithOnePerson(stalls, first=True)
        else:
            idx = fillStallWithOnePerson(stalls)
    
    Rs = computeRs(stalls, idx)
    Ls = computeLs(stalls, idx)
    
    return min(Rs, Ls), max(Rs, Ls)
        
        
def initStalls(n):
    stalls = [False] * (n+2)
    stalls[0] = True
    stalls[n+1] = True
    
    return stalls

if __name__ == '__main__':
    # input() reads a string with a line of input, stripping the '\n' (newline) at the end.
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        n, k = [int(s) for s in input().split(" ")]
        
        minSpace, maxSpace = fillStallWithKPerson (n, k)
        
        print("Case #{}: {} {}".format(i, maxSpace, minSpace))
        # check out .format's specification for more formatting options