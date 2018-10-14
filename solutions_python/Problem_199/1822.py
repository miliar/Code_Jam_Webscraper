# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 13:48:08 2017

@author: LeaPim
"""
def flip(pancakes, beg, ends):
    for i in range(beg, ends + 1):
        if(pancakes[i] == '+') :
            pancakes[i] = '-'
        else :
            pancakes[i] = '+'
    return pancakes;
    
#input
n = int(input())

for i in range (n) :
    line = input().split()
    pancakes = list(line[0])
    k = int(line[1])
    flip_counter = 0
    
    #remove the plus at the border of pancakes
    while(len(pancakes) > 0 and pancakes[0] == '+'):
           pancakes = pancakes[1:]
    
    
    while(len(pancakes) >= k):
        pancakes = flip(pancakes,0, k-1)
        flip_counter += 1
        while(len(pancakes) > 0 and pancakes[0] == '+'):
           pancakes = pancakes[1:]
        
    if(len(pancakes) == 0):
        print("Case #{}: {}".format(i+1,flip_counter))
    else :
        print("Case #{}: IMPOSSIBLE".format(i+1))


