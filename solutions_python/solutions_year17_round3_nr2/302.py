# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 08:47:28 2017

@author: kprashan
"""

T = int(input().rstrip())
speedForAnnie = 1.0000000000

for i in range(1,T+1):
    j,k = [int(num) for num in input().strip().split()]
    array = []
    for a in range(j+k):
        s,e = [int(num) for num in input().strip().split()]
        array.append((s,e))
    if j == 1 or k == 1 :
        print("Case #{}: {}".format(i,2))
    elif (j==0) and (k==0):
        print("Case #{}: {}".format(i,2))
    else:
        array.sort(key=lambda tup:tup[0])
        if min(abs(array[-1][-1] - array[0][0]),abs(array[0][1] + 1440 - array[1][0])) > 720 :
            print("Case #{}: {}".format(i,4))
        else :
            print("Case #{}: {}".format(i,2))