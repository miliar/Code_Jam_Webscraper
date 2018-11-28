# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 08:50:12 2017

@author: kprashan
"""
import operator 

T = int(input().rstrip())
color = "ROYGBV"
for i in range(T):
    N, R, O, Y, G, B,V = [int(num) for num in input().rstrip().split()]
    arrDict = {}
    placeDict = {}
    string = ''
    arr = [R, O, Y, G, B,V]
    
    for z in range(len(color)) :
        arrDict[color[z]] = arr[z]
    
    k = 0
#    print('arrDict',arrDict)
    for l,items in enumerate(sorted(arrDict.items(), key=operator.itemgetter(1), reverse=True)):
        for j in range(items[1]):
            if k >= N :
                k = 1
            placeDict[k] = items[0]
            k = k + 2
            
    
#    print('placeDict',placeDict)
    impos = False
    for j in range(N):
        string += placeDict[j]
        
    for idx in range(len(string)-1) :
        if string[idx] == string[idx+1] :
            impos = True
            
    if string[0] != string[-1] and (not impos) :    
        print("Case #{}: {}".format(i+1, string))
    else :
        print("Case #{}: {}".format(i+1, 'IMPOSSIBLE'))
        