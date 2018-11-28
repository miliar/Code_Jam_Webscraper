import os,sys

invertsWith = {}
combineResult = {}

def populateDicts(case):
    case = case.split() 
    n = int(case.pop(0))
    for i in range(n):
        c = case.pop(0)        
        combineResult[(c[0],c[1])]= c[2]
        combineResult[(c[1],c[0])]= c[2]
    n = int(case.pop(0))
    for i in range(n):
        c = case.pop(0)
        try:
            invertsWith[c[0]].append(c[1])
        except KeyError:
            invertsWith[c[0]] = [c[1]]
        try:
            invertsWith[c[1]].append(c[0])
        except KeyError:
            invertsWith[c[1]] = [c[0]]
    return case[-1]

def invokeElement(currentList, c):
    currentList.append(c)
    if len(currentList) > 1:
        try:
            k = combineResult[(currentList[-1],currentList[-2])]
            currentList.pop()
            currentList.pop()
            currentList.append(k)            
        except KeyError:
            pass
    if len(currentList) > 1:
        try:
            inv = invertsWith[currentList[-1]]
            for i in range(0,len(currentList)-1):
                if currentList[i] in inv:                    
                    return []
        except KeyError:
            pass        
    return currentList

def getResult(c):
    res = []
    for i in c:
        res = invokeElement(res,i)     
    return res

inputFile = open('b-small.in','r')
sys.stdin = inputFile
output = open('b-small.out','w')
t = int(input())
for i in range(t):
    invertsWith = {}
    combineResult = {}
    case = input()
    case = populateDicts(case)
    print('Case #' + str(i+1) + ': ' + str(getResult(case)).replace("'",""), file = output)
output.close()
inputFile.close()

    
    
