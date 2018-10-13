# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 11:35:56 2017

@author: Doris
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 10:56:51 2017

@author: Doris
"""

def mini(min_arr, max_arr):
    length = len(min_arr)
    min_index = 0
    for i in range(length):
        if(min_arr[i] > min_arr[min_index]):
            min_index = i
        elif(min_arr[i] == min_arr[min_index] and max_arr[i] > max_arr[min_index]):
            min_index = i
    return min_index

T = int(input())

for t in range(T):
    temp = (input().split())
    N = int(temp[0])
    K = int(temp[1])
    #print(N, K)
    min_array = [0]*N
    max_array = [0]*N
    Rs = [0]*N
    Ls = [0]*N
    occupied = [0]*N
    
    for i in range(N):
        Rs[i] = N-1-i
        Ls[i] = i
        min_array[i] = min(Rs[i], Ls[i])
        max_array[i] = max(Rs[i], Ls[i])
        
    #print(Rs, Ls)
    #print(min_array, max_array)
    
    for i in range(K-1):
        index = mini(min_array, max_array)
        occupied[index] = 1
        Rs[index] = 0
        Ls[index] = 0
        min_array[index] = 0
        max_array[index] = 0
        for j in range(index):    # the left side
            if Rs[index-j-1] < j:
                break
            Rs[index-j-1] = j
            min_array[index-j-1] = min(Rs[index-j-1], Ls[index-j-1])
            max_array[index-j-1] = max(Rs[index-j-1], Ls[index-j-1])
        for j in range(N-index-1):
            if Ls[index+j+1] < j:
                break
            Ls[index+j+1] = j
            min_array[index+j+1] = min(Rs[index+j+1], Ls[index+j+1])
            max_array[index+j+1] = max(Rs[index+j+1], Ls[index+j+1])
        #print(Ls, Rs, min_array, max_array)  
    
    
    i = mini(min_array, max_array)
    out = "Case #%d: %d %d"%(t+1, max_array[i], min_array[i])
    print(out)



