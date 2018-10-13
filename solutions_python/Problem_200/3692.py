# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 17:29:42 2017

@author: User
"""

import sys

def getNumber(line):
    listNum=list(line)
    for i in range(len(listNum)-2,-1,-1):
        if int(listNum[i]) > int(listNum[i+1]):
            for j in range(i+1,len(listNum)):
                listNum[j]="9"
            if (int(listNum[i])>0 and i !=0) or (int(listNum[i])>1 and i ==0):
                listNum[i]=str(int(listNum[i])-1)                
            elif (int(listNum[i])==0 and i!=0):
                listNum[i]="9"
                for k in range(i-1,-1,-1):
                    if int(listNum[k]) >0 and k!=0:                     
                        listNum[k]=str(int(listNum[k])-1)
                        break
                    elif int(listNum[k]) ==0 and k!=0:
                        listNum[k]="9"
                    else:
                        listNum[k]=""  
                        
                        
                    
            else:
                listNum[i]=""
                
    return "".join(listNum)

out=open(sys.argv[1]+"_result","w+")
result =[]
with open(sys.argv[1]) as f:
    lines = f.read().splitlines()
num_cases=int(lines[0])

for i in range(1,len(lines)):
    temp= "Case #" + str(i)+ ": " + str( getNumber(lines[i]))
    
    #print(temp)
    result.append(temp)     
out.write("\n".join(result))
out.close()