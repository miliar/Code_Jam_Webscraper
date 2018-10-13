'''
Created on Apr 13, 2014

@author: ahmed
'''
import copy
inFile=open("B-small-attempt0.in","r")

outFile=open("QualRound_BSmall.out","w")

Lines=inFile.readlines()
TestCaseNo=int(Lines[0])
print TestCaseNo
Lines=Lines[1:]  
for i in range(TestCaseNo):
    CookiesIn=Lines[i]
    CookiesIn=CookiesIn.split()
    C=float(CookiesIn[0])
    F=float(CookiesIn[1])
    X=float(CookiesIn[2])
#     print C, F, X
    nFarms=0
    TotFarmCost=0
    FarmTime=C/2
    T_FarmFuture=[]
    T_FarmNow=[]
    FarmProductionNow=2
    for j in range(int(X)): 
        T_wMaybe=X/(FarmProductionNow)+sum(T_FarmNow) 
        FarmProductionFuture=FarmProductionNow+F
        T_FarmFuture+=[C/(FarmProductionNow)]
        T_Futadded=X/(FarmProductionFuture)+sum(T_FarmFuture)
        if T_Futadded<T_wMaybe:
            T_FarmNow+=[C/(FarmProductionNow)]
            FarmProductionNow=FarmProductionFuture
        else:
            print>>outFile,"Case #%s: "%(i+1), T_wMaybe
            break