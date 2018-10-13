'''
Created on Apr 12, 2014

@author: marknorton
'''

file = open("text.txt")


testCases = int(file.readline())

data = []
for tNum in range(1,testCases+1):
    data.append(file.readline().split())
    C = float(data[tNum - 1][0])
    F = float(data[tNum - 1][1])
    X = float(data[tNum - 1][2])
    money = 0.0
    ans = -1
    currentRate = 2.0
    totalTime = 0.0
    
    
    if X < C:
        ans = X/currentRate
    
    calc = C/currentRate + X/(currentRate + F)
    #time to get 
    while calc < X/currentRate:
        totalTime += C/currentRate
        currentRate += F
        calc = C/currentRate + X/(currentRate + F)
        
    totalTime += X/(currentRate)
    
        
        
    print("Case #{}: {:.7f}".format(tNum,totalTime))
        
        
    
    
    