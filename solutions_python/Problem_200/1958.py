# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 15:23:40 2017

@author: LeaPim
"""

def compare(first, second):
    if(first > second):
        return 1
    elif(first == second):
        return 0
    else:
        return -1

def put_nine(liste):
    return [9]* len(liste)


n = int(input())

for i in range (n) :
    number = list(map(int,input()))
    
    incr = 0
    ptr_cmp = 1
    
    while(1):
        if(incr + ptr_cmp >= len(number)):
            break
        comp = compare(number[incr],number[incr + ptr_cmp])
        if(comp == 0) :
            ptr_cmp += 1
        elif(comp == 1):
            number[incr] -=1
            number [incr+ 1:] = put_nine(number[incr + 1:])
            break
        else:
            incr += ptr_cmp
            ptr_cmp = 1
    
            
    while(len(number) > 1 and number[0] == 0):
        number = number[1:]
        
    my_string = ""
    for j in number :
        my_string += str(j)
        
    print("Case #{}: {}".format(i+1,my_string))
   
