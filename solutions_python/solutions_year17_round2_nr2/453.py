# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 18:31:12 2017

@author: Robbe Sneyders
"""
from operator import itemgetter


def answer(n, horses):
    
    color=['R','O','Y','G','B','V']
    
    if max(horses) > n/2:
        return 'IMPOSSIBLE'
    
    index, element = argmax(horses)             
    horses[index] -= 1
    horses = horses[index:] + horses[:index]
    color = color[index:] + color[:index]
    
    solution = color[0]
    previous = 0    
    
    for i in range(n-1):
        if previous == 0:
            index, element = argmax([0, 0] + horses[2:-1] + [0])
        else:
            index, element = argmax(horses[:previous-1] + [0, 0, 0] + horses[(previous+2):])
        
        solution += color[index]          
        horses[index] -= 1
        previous = index
            
    return solution
                
    
def argmax(list):
     return max(enumerate(list), key=itemgetter(1))

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    horses = [int(s) for s in input().split(" ")]
    n = horses.pop(0)
    
    solution = answer(n, horses)
    print("Case #{}: {}".format(i, solution))