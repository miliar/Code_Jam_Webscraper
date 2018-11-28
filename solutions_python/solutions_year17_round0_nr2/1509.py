# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 21:21:00 2017

@author: kprashan
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 20:32:09 2017

@author: kprashan
"""
def find_tidy(n):
    if len(n)== 1 :
        return n
    tidy = False
    while not tidy :
        tidy = True
        for i in range(len(n)-1):
            if n[i] <= n[i+1]:
                continue
            else :
                n = n[0:i] + str(int(n[i])-1) + '9'*len(n[i+1:])
                tidy = False
                break
    return int(n)
    
        
file_in = "B-large.in"
array = []
with open(file_in) as f :
    for line in f :
        array.append(line.rstrip())
        
#for line in array :
#    print(line)        
n = int(array[0])
fileOut = open("outB-large.txt","w")
for i in range(1,n+1):
#    print(array[i])
#    print("Case #{}: {}".format(i,array[i].rstrip()))
#    print("Case #{}: {}".format(i,find_tidy(array[i].rstrip())))
    print("Case #{}: {}".format(i,find_tidy(array[i].rstrip())),file=fileOut)
fileOut.close()
#    print("Case #{}: {}".format(i,find_tidy),file=fileOut)
