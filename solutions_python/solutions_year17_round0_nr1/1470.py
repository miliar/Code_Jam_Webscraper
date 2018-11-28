# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 19:15:25 2017

@author: Sully
"""

def flip(s):
    return s.translate(str.maketrans('+-','-+'))

def solve(l):
    flips = 0
    flipper_size = int(l[1])
    pancakes = l[0]
    if pancakes.count('+') == len(pancakes):
        return str(0)
    for j in range(len(pancakes)):
        if pancakes[j] == '-':
            if j+flipper_size > len(pancakes):
                break
            pancakes = pancakes[0:j] + flip(pancakes[j:j+flipper_size]) + pancakes[j+flipper_size:]
            #print (pancakes)
            flips+=1
    if '-' in pancakes:
        return 'IMPOSSIBLE'
    return str(flips)

import sys
#f = open('qual1in.txt','r')
f = open('qual1large.txt','r')
f.readline()
i=1
for line in f:
    #print (line.strip())
    print ('Case #'+str(i)+': ' + solve(line.strip().split(' ')))
    i+=1
    