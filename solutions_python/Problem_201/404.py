# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 11:03:20 2017

@author: 修修
"""

# -*- coding: utf-8 -*-

with open("C-large.in", "r") as f:
    filein = f.readlines()
        
def findExp(K):
    exp = 1
    while (K>>1) != 0:
        exp+=1
        K= K>>1
    #print (exp)
    return exp

t = int(filein[0])  # read a line with a single integer
for cnt in range(1, t + 1):
    ans = 0
    N, K = [int(s) for s in filein[cnt].split(" ")]
    #N, K = 8, 4
    #print (N, K) 
    
    expK = findExp(K)
    
    maxLR = N//(2**expK)
    #print("maxlr"+str(maxLR))
    
    Diff1Num = (maxLR*(2**expK) + (2**expK)-1) - N
    #print("Diff1Num"+str(Diff1Num))
               
    #print((2**expK)-Diff1Num)

    if K < (2**expK)-Diff1Num:
        y = maxLR
        z = y
    else:
        y = maxLR
        z = y - 1
        
    if K >= (2**expK)-(Diff1Num - ((2**expK)>>1)):
        y = y - 1
    print ("Case #{}: {} {}".format(cnt, y, z))
    
    
    
    
    
"""
    # -*- coding: utf-8 -*-
"""
#Created on Sat Apr  8 11:03:20 2017

#@author: 修修
"""

# -*- coding: utf-8 -*-

with open("C-small-2-attempt0.in", "r") as f:
    filein = f.readlines()
        
t = int(filein[0])  # read a line with a single integer
for cnt in range(1, t + 1):
    ans = 0
    N, K = [int(s) for s in filein[cnt].split(" ")]
    print (N, K) 
    brList = [N]
    if K>N/2:
        print ("Case #{}: {} {}".format(cnt, 0, 0))
        continue
    for people in range(K-1):     
        #print("people")
        if brList[0] & 1:#odd
            brList.append((brList[0]-1)//2)
            brList.append((brList[0]-1)//2)
        else:
            brList.append(brList[0]//2)
            brList.append((brList[0]//2)-1)
        #print (brList)
        del brList[0]
        #brList.sort(reverse=True)
        maxInList = 0#brList[0]
        maxIdx = 0
        for idx in range(len(brList)):
            if brList[idx] > maxInList:
                maxInList = brList[idx]
                maxIdx = idx
        brList[0],brList[maxIdx]=brList[maxIdx],brList[0]
        
        #print (brList)
    if brList[0] & 1:#odd
        y = (brList[0]-1)//2
        z = y
    else:
        y = brList[0]//2
        z = y-1

    print ("Case #{}: {} {}".format(cnt, y, z))
    """