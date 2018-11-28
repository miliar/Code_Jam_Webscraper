# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 20:04:20 2017

@author: willedwa
"""

def solve(N):
    #print('Starting number: ' + str(N))
    c = []
    for digit in N:
        c.append (int(digit))
    for i in range(len(c)-1):
        #print('len(c)-i: ' + str(len(c)-i))
        #print('c[last]: ' + str(c[len(c)-i-1]))
        #print('c[2nd to last]: ' + str(c[len(c)-i - 2]))
        if c[(len(c)-i-1)] < c[(len(c)-i-2)]:
            c[len(c)-i-2 ] -= 1
            for j in range(i+1):
                c[len(c)-j-1] = 9
            #print('Updated number: ' + str(c))
    ltidynumber = ''.join(str(x) for x in c)      
    answer = ltidynumber.lstrip("0")
    return answer
  


T = int(input())
#print('Number of Cases: ' + str(T))
for t in range(T):
    N = input()
    print ('Case #' + str(t+1) + ': ' + solve(N))