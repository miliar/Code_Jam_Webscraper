# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 20:16:25 2017

@author: willedwa
"""

def solve(N):
    set = N.split()
    N = int(set[0])
    K = int(set[1])
    #print('Number of stalls: ' + str(N))
    #print('Number of people about to enter: ' + str(K))
    large_gap = N
    gaps = [large_gap]
    counts = [1]
    newL_gap = 0
    newS_gap = 0
    i = 0
    while K > i:
        maxIndex = gaps.index(max(gaps))
        numMaxInst = counts[maxIndex]
        oldi = i
        i = i + numMaxInst
        #print('i + numMaxInst =' + str(oldi) + '+' + str(numMaxInst) + '=' + str(i)) 
        if max(gaps) > 1 and max(gaps)%2 == 0:
           newL_gap = float(max(gaps)/2)
           newS_gap = float(max(gaps)/2-1)
        elif max(gaps) > 1 and max(gaps)%2 == 1:
           newL_gap = float((max(gaps)-1)/2)
           newS_gap = float((max(gaps)-1)/2)
        else:
            newL_gap = 0
            newS_gap = 0
        if K <= i:
            #print('Exiting because K<=i: ' + str(K) + ' ' + str(i))
            break
        else:        
            del gaps[maxIndex]
            del counts[maxIndex]
            if gaps.count(newL_gap) > 0:
                counts[gaps.index(newL_gap)] += numMaxInst
            else:
                gaps.append(newL_gap)
                counts.append(numMaxInst)
            if newS_gap > 0 and gaps.count(newS_gap) > 0:
                counts[gaps.index(newS_gap)] += numMaxInst
            else:
                gaps.append(newS_gap)
                counts.append(numMaxInst)
            #print('gaps, counts, i: '  + str(gaps) + str(counts) + str(i))
    return str(int(newL_gap)) +' ' +str(int(newS_gap))
  


T = int(input())
#print('Number of Cases: ' + str(T))
for t in range(T):
    N = input()
    print ('Case #' + str(t+1) + ': ' + solve(N))