# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 14:05:43 2017

@author: Özcan
"""
import math 

def next_lower_power_of_2(x):  
    return 2**((int(x)).bit_length()-1)

def create_decisiontree(K):
    bin_vector = list()
    while K != 1:
        # find distance from closest power of two
        power = next_lower_power_of_2(K)
        dist = K - power
        if dist >= power/2:
            bin_vector.append(1)
            K = dist
        else:
            bin_vector.append(0)
            K = int(dist+power/2)
    return bin_vector

def split_stalls(N, vector):
    for i in range(len(vector)-1,-1,-1):
        N = (N-1)/2
        if vector[i]==0:
            N = math.ceil(N)
        else:
            N = math.floor(N)
    N = (N-1)/2
    result = (math.ceil(N), math.floor(N))
    return result

def solve(N,K):
    treevector = create_decisiontree(K)
    result = split_stalls(N, treevector)
    return result

numberCases = int(input())

for i in range(1,numberCases+1):
    N, K = [int(s) for s in input().split(" ")]
    result = solve(N, K)
    print("Case #{}: {} {}".format(i, result[0], result[1]))