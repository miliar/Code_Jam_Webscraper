'''
Created on Apr 12, 2014

@author: marknorton
'''

def closest(K,item):
    w = 2
    for x in K:
        if x > item and x < w:
            w = x
    
    return w

def compare(N,K):
    for k,x in enumerate(N):
        if x < K[k]:
            return False
    return True

def winOrLose(data,data2):
    olen = len(data[0])
    N = [float(x)for x in data[0]]
    K = [float(x)for x in data2[0]]
    
    N.sort()
    K.sort()
    
    NewList = list(N)
    newK = list(K)

    result1,result2 = 0,0
    
    while not compare(N,K):
        N.remove(min(N))
        K.remove(max(K))
    
    result1 += len(K)
    init = 2
    while len(NewList) != 0:
        item1 = NewList.pop()
        for x in newK:
            if x > item1 and x < init:
                init = x
        
        if item1 < init and init != 2:
            result2 +=1 
        else:
            newK.remove(min(newK))
        
        if init != 2 :
            newK.remove(init)
        init = 2
    result2 = olen -result2
    return result1, result2

file = open("text.txt")


testCases = int(file.readline())

data = []
data2 = []
for tNum in range(1,testCases+1):
    blocks = int(file.readline())
    data.append(file.readline().split())
    data2.append(file.readline().split())
    
    p1, p2 = winOrLose(data, data2)
    data = []
    data2 = []
        
    print("Case #{}: {} {}".format(tNum,p1,p2))
        
        
    
    
    