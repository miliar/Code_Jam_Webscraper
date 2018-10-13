# -*- coding: utf-8 -*-
"""
Created on Sun Apr 09 02:47:33 2017

@author: AliFurkan
"""


def convert(arr):
    arr = [arr[j] for j in xrange(len(arr))]
    
    for j in xrange(len(arr)):
         if arr[j]=="-":
             arr[j]=0
         else:
            arr[j]=1

    return arr
fname = "C:\Users\AliFurkan\Downloads\A-large.in"    
i = 1
with open(fname) as f:
    T = int(f.readline())
    for line in f:
         arr, per = line.split()
         per = int(per)
         arr = convert(arr)
         counter = 0
         for j in xrange(len(arr)-per+1):
             if arr[j] == 0:
                 arr[j:j+per] = [k^1 for k in arr[j:j+per]]
                 counter += 1
         if sum(arr) == len(arr):
             print "Case #%d: %d" % (i, counter)
             
         else:
             print "Case #%d: IMPOSSIBLE" % (i)  
         i += 1
