#!/usr/bin/python3

def isTidy(numList):
    for i in range(0, len(numList) - 1):
        if numList[i] > numList[i+1]:
            return False
    return True

tc = int(input(""))
if tc > 0 and tc <= 100:
    for test in range(tc):
        n = int(input(""))
        
        while not isTidy(list(str(n))):
            n = n-1
            
        print("Case #"+ str(test+1) + ": " + str(n))