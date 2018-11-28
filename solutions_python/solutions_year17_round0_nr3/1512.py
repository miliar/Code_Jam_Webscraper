# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 15:38:01 2017

@author: Sully
"""


#def split_interval(i):
#    mid = i[1]/2
    


def solve(l):
    #print(l)
    
    num_stalls = int(l[0])
    num_people = int(l[1])
    
    stall_intervals ={num_stalls:1}
    #print (stall_intervals)
    
    
    for i in range(num_people-1):
        #print(list(stall_intervals.keys()))
        best_interval = max(list(stall_intervals.keys()))
        if stall_intervals[best_interval] == 1:
            stall_intervals.pop(best_interval)
        else:
            stall_intervals[best_interval] = stall_intervals[best_interval] -1
            
        
        new1 = best_interval//2
        
        if best_interval %2:
            new2 = new1
        else:
            new2 = new1-1
            
        for x in new1,new2:
            if x in stall_intervals:
                stall_intervals[x] = stall_intervals[x] + 1
            else:
                stall_intervals[x] = 1
    #print (stall_intervals)
            
    m = max(list(stall_intervals.keys()))
    
    
    if m==1:
        return '0 0'
    
    if m==2:
        return '1 0'
    
    if m%2:
        return str(m//2)+' '+str(m//2)
    else:
        return str(m//2)+' '+str(m//2-1)
    
    #return str(m)
    #return str(m//2)+' '+str(max(m//2-1,0))
    #return str(max(m//2,m//2-1))+' '+str(min(m//2,m//2-1))




import sys
f = open('qual3medin.txt','r')
#f = open('qual3smallin2.txt','r')
#f = open('qual3smallin.txt','r')
f.readline()
i=1
for line in f:
    print ('Case #'+str(i)+': ' + solve(line.strip().split(' ')))
    i+=1