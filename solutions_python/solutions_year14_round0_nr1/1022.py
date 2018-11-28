#-*- coding:utf-8 -*-
'''
Created on 2014年4月12日

@author: wilbur
'''
import string




def getCommon(listA,listB):
    counter =[]
    for i in listA:
        if i in listB:
            counter.append(i)
    return counter

f=open(r'F:A-small-attempt0.in')
fw=open(r'F:\A-small.out','w')
caseNum=string.atoi(f.readline()) 



  
#测试caseNum个case
for i in range(caseNum): 
    rowNOA=string.atoi(f.readline())  
    listA=[]
    for j in range(4):
        temp = f.readline().strip().split()
        listA.append(temp) 
    rowNOB=string.atoi(f.readline()) 
    
    listB=[]
    for k in range(4):
        temp = f.readline().strip().split()
        listB.append(temp) 
     
    common= getCommon(listA[rowNOA-1],listB[rowNOB-1])
    
    if len(common)==0:
        fw.write('Case #{}: Volunteer cheated!\n'.format(i+1))
    elif len(common)==1:
        fw.write('Case #{0}: {1}\n'.format(i+1,common[0]))
    else:
        fw.write('Case #{}: Bad magician!\n'.format(i+1))
    
f.close()
fw.close()