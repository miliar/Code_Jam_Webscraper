from __future__ import division
import math
import sys
from copy import *
sys.stdin = open("input1l.in","r")
sys.stdout = open("output1l.out","w")

def get_area(l,i,k,r):
    l.remove(l[i])
    g=[]
    for j in range(len(l)):
        if l[j][0]<=r:
            g += [ (l[j][0]*l[j][1])]
    if len(g)<k-1:
        return -1
    g.sort(reverse=True)
    sum_=0
    for j in range(k-1):
        sum_ += g[j]
    return 2*sum_
        
test = int(raw_input())

for t in range(test):
    n,k=map(int,raw_input().split())
    rk = [[0,0] for i in range(n)]# rk = rh
    for i in range(n):
        rk[i][0],rk[i][1]=map(int,raw_input().split())
    
    max_ = 0
    for i in range(n):
        curr_radius = rk[i][0]
        curr_height = rk[i][1]
        new_max = curr_radius*curr_radius + 2*curr_radius*curr_height + get_area(deepcopy(rk),i,k,curr_radius)  ## sum of 2*ri * hi
        max_ = max(new_max,max_)
        
    print "Case #"+str(t+1)+":",
    print ("%.9f"%(math.pi*max_))
    
    
        
        
    
