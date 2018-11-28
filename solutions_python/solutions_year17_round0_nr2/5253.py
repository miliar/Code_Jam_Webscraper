# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 10:08:36 2017

@author: rmcm

Tidy Numbers

"""
def finding_Tidy(n):
    
    numberTidy = -1    
    number = int(n)
    isTidy = True
    for i in range(number,0,-1):
        x = str(i)        
        for j in range(len(x)-1):
            if x[j]<=x[j+1]:
                isTidy = True
            else:
                isTidy = False
                break
        if isTidy:
            numberTidy = i
            break
    return numberTidy

            
    



data_in = open('B-small-attempt1.in', 'r')
data_out = open ('PB_Tidy_out.txt', 'w')

T = int(data_in.readline())

for i in range(T):
    N = data_in.readline().strip()
    tidy2 = finding_Tidy(N)
    print("Case #{}: {}".format(i+1,tidy2), file=data_out)
    print("Case #{}: {}".format(i+1,tidy2))
    
    
