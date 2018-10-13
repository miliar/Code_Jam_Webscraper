# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 09:54:18 2017

@author: Doris
"""
count = input()

#print(length)
for j in range(int(count)):
    num = input()
    num = list(num)
    length = len(num)
    while(1):
        flag = 0
        for i in range(length-1):
            if(flag == 1):
                num[i] = '9'
            elif(int(num[i]) > int(num[i+1])):
                flag = 1
                num[i] = str(int(num[i]) - 1)
                num[length-1] = '9'
       # print(num)
        if(flag == 0):
            break
        flag = 0
    out = "Case #%d: %d"%(j+1, int("".join(num)))
    print(out)
    #print("Case #", j+1, ":", int("".join(num)))
  



