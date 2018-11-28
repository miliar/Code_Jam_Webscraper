# -*- coding: utf-8 -*-
"""
python stdin_test.py < input.txt > output.txt 
"""
import sys



def DetTidy(aNum):
    lst = list(aNum)
    broken = -1
    
    ln = len(lst)
    for l in range(1, ln):
        
        if(int(lst[l]) < int(lst[l-1]) ):
            broken = l
            break
        
    if broken == -1:
        return aNum
    else:
        tempArr = []
        
        for i in range(broken, ln):
            tempArr.append(int(lst[i]))
        
        num = int(''.join(map(str,tempArr)))
        
        tidy = int(aNum) - num - 1
        
        return DetTidy(str(tidy))
    

#t = int(sys.stdin.readline())
lines = sys.stdin.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].replace('\n','')
    


T = int(lines[0])

results = []

for i in range(1,T+1):
    tidy = DetTidy(lines[i])
    results.append(tidy)
#    print(tidy)
#
#for i in range(1,T+1):
#    print(i, results[i-1])
#    
    
for i in range(1,T+1):
    print("Case #{}: {}".format(i, results[i-1]))