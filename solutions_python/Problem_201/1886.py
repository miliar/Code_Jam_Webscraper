# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 16:48:46 2017

@author: LeaPim

"""
from queue import PriorityQueue
from math import floor

n = int(input())

for i in range (n) :
    q = PriorityQueue()
    line = input().split()
    nb_stall = int(line[0])
    nb_user = int(line[1])
    
    q.put((-nb_stall,nb_stall))

    for person in range(nb_user-1) :
        cur = q.get()
        cur = cur[1]
        q.put((-floor(cur/2),floor(cur/2)))
        q.put((-floor((cur-1)/2),floor((cur-1)/2)))
    cur = q.get()
    cur = cur[1]
    zero = (floor((cur-1)/2))
    print("Case #{}: {} {}".format(i+1,floor(cur/2),zero))









