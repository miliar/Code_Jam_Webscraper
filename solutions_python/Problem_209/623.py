# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 08:47:28 2017

@author: kprashan
"""
import math
from itertools import combinations
def get_area(r,h):
    return r**2 + 2*r*h

def get_total_area(array,k):
    sorted_arr = sorted(array,key=lambda tup:tup[2],reverse=True)
    ksort = sorted_arr[0:k]
    ksort.sort(key=lambda tup:tup[0])
    
    area = get_area(ksort[0][0],ksort[0][1])
#    print(ksort)
    for i in range(1,k) :
        diff = ksort[i][0]**2 - ksort[i-1][0]**2
        area += diff + 2*ksort[i][0]*ksort[i][1]
    
    return math.pi * area
        
T = int(input().rstrip())
speedForAnnie = 1.0000000000

for i in range(1,T+1):
    n, k = [int(num) for num in input().strip().split()]
    rh = []
    for j in range(n):
        radius,height =  [int(num) for num in input().strip().split()]
        rh.append((radius,height,get_area(radius,height)))
    tuples = combinations(rh,k)
    area = max([get_total_area(tup,k) for tup in tuples])
    #area=get_total_area(rh,k)
    print("Case #{}: {}".format(i,area))