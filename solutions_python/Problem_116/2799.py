# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 06:14:39 2013

@author: Administrator
"""
import pdb

import csv as csv
Completed = True
def IsLike(Symbol,Checked):
    global Completed
    if (Checked == Symbol or Checked =='T'):
        return True
    else:
        return False
def CheckRow(Table,Row):
    global Completed
   
    j =0
    Sym=Table[Row][j]
    if Sym=='T':
        Sym=Sym=Table[Row][j+1]
    OutCome = True
    if (Sym) !='.':
        for j in range(1,3+1):
            OutCome*=IsLike(Sym,Table[Row][j])
            if Table[Row][j] == '.':
                Completed = False
                      
    else:
        Completed = False
    if OutCome == True:
        return Sym
    

def CheckDiag(Table,TB):
    global Completed
    j =0
    Sym=Table[TB-j][j]
    if Sym=='T':
        

        if TB==0:
            
            Sym=Table[TB-j+1][j+1]
        if TB==3:
           Sym=Table[TB-j-1][j+1] 
        
    
    OutCome = True
    if (Sym) !='.':
        for j in range(1,3+1):
            if TB==0:
                OutCome*=IsLike(Sym,Table[j][j])
            else:
                OutCome*=IsLike(Sym,Table[j][TB-j])
                
            if Table[TB-j][j] == '.':
                Completed = False
                      
    else:
        Completed = False        
    if OutCome == True:
        return Sym
def CheckCom(Table,Com):
    global Completed
   
    j =0
    Sym=Table[j][Com]
    if Sym=='T':
        Sym=Sym=Table[j+1][Com]
    OutCome = True
    if (Sym) !='.':
        for j in range(1,3+1):
            OutCome*=IsLike(Sym,Table[j][Com])
            if Table[j][Com] == '.':
                Completed = False
                      
    else:
        Completed = False
    if OutCome == True:
        return Sym
    
def Check(Array):
    
    global Completed
    D={}
    D['.']=0
    D['X']=0
    D['O']=0
    for i in range (0,3+1):
        
        Sym = CheckRow(Array,i)
        if Sym!= None:
            D[Sym]+=1
        Sym = CheckCom(Array,i)
        if Sym!= None:
            D[Sym]+=1
    Sym = CheckDiag(Array,0)
    if Sym!= None:
        D[Sym]+=1
    Sym = CheckDiag(Array,3)
    if Sym!= None:
        D[Sym]+=1
    if D['X']==D['O']:
        if Completed == False:
            return 'Game has not completed'
        else:
            return 'Draw'
    else:
        if D['X']>D['O']:
            return 'X won'
        else:
            return 'O won'
path = ('E:\\pythondata\\A-small-practice.in')   
InPath = csv.reader(open(path,'rb'),delimiter=' ',quotechar='|')      

NumCases= int(InPath.next()[0])
print NumCases
f = open('E:\\pythondata\\OutFIle.txt', 'r+')
for Case in range (1, NumCases+1):
    CaseAr=[['.','.','.','.'],['.','.','.','.'],['.','.','.','.'],['.','.','.','.']]
    S=''
    S+= "Case #"+str(Case)+": "
    i=0
    
    for line in range ((Case-1)*5,Case*5-1):
        
        Completed =True
        Next =InPath.next()[0].split()
        if Next[0] !='':
            CaseAr[3-i]=Next[0]
        i+=1
    try :
        Next =InPath.next()
    except:
        print""
    

    S+=Check(CaseAr)+'\n'
    f.write(S)
    
    print (S)    
        
        
    