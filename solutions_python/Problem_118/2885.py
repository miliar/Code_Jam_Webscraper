# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 14:31:20 2013

@author: Administrator
"""
import numpy  as np
import csv as csv
import pdb
def IsFair(word):
    word = str(word)
    if len(word) < 2: return True
    if word[0] != word[-1]: return False
    return IsFair(word[1:-1])
def GetRange(Left,Right):
    
    NLeft=(np.sqrt(Left))
    if NLeft.is_integer():
        NLeft=NLeft
    else:
        NLeft=np.ceil(NLeft)
        
    NRight=((np.sqrt(Right)))
    if NRight.is_integer():
        NRight+=1
    else:
        NRight = np.ceil(NRight) # the boundry
        
   
    print (NLeft,"=",NRight)
    return range(int(NLeft),int(NRight))

def Check(Num):
    
    if IsFair(Num**2):
        if IsFair(Num):
            return True
    else:
        return False
path = ('E:\\pythondata\\A-small-practice.in')   
InPath = csv.reader(open(path,'rb'),delimiter=' ',quotechar='|')      
i =0
Count =0
f = open('E:\\pythondata\\OutFIle.txt', 'r+')
for Row in InPath:
    
    if i >0:
        Range = GetRange(int(Row[0]),int(Row[1]))
        Count =0
        for Num in Range:
            
            if  Check(Num) == True:
                Count +=1
    
        S ='Case #'+str(i)+': '+str(Count)+"\n"
        print(S)    
        f.write(S)
    i+=1

    