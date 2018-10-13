#-*- coding:utf-8 -*-

import string

def deceitfulWar(listA,listB):
    
    score = 0
    for mass in listB:
        if mass >listA[len(listA)-1]:
            score +=0
            listA.pop(0)
        else:
            for i in range(len(listA)):
                if mass <listA[i]:
                    score +=1
                    listA.pop(i)
                    break
    return score
        
    

def war(lista,listb):
    listA =lista
    listB = listb
    score = 0
    for mass in listA:
        if mass >listB[len(listB)-1]:
            score +=1
            listB.pop(0)
        else:
            for i in range(len(listB)):
                if mass <listB[i]:
                    score +=0
                    listB.pop(i)
                    break
    return score



f=open(r'F:\D-large.in')
fw=open(r'F:\D-large.out','w')
caseNum=string.atoi(f.readline()) 



  
#测试caseNum个case
for i in range(caseNum): 
    f.readline()
    listA = f.readline().strip().split()
    listB = f.readline().strip().split()
    listC = []
    listD = []
    for j in range(len(listA)):
        listA[j] = string.atof(listA[j])
        listC.append(listA[j])
    for j in range(len(listB)):
        listB[j] = string.atof(listB[j])
        listD.append(listB[j])
    listA.sort()
    listB.sort()
    listC.sort()
    listD.sort()
    fw.write('Case #%d: %d %d\n' %(i+1,deceitfulWar(listA,listB),war(listC,listD)))

f.close()
fw.close()