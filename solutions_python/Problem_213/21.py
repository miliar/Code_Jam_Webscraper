from sys import stdin as cin
from copy import deepcopy as cp
from math import ceil

data=cin.readline

def maxIndex(nums):
    index=0;
    for i in range(1, len(nums)):
        if nums[i]>nums[index]:
            index=i
    return index

cases=int(data());

for case in range(1, cases+1):
    line=data().split()
    seats=[0 for i in range(int(line[0])+1)]
    customers=[0 for i in range(int(line[1])+1)]
    tickets=int(line[2])
    for i in range(tickets):
        line=data().split()
        seats[int(line[0])]+=1
        customers[int(line[1])]+=1
    rides=max(max(customers), int(ceil(tickets/(len(seats)-1))))
    pseats=cp(seats)
    while pseats[maxIndex(pseats)]>rides:
        index=maxIndex(pseats)
        while index>0 and pseats[index]>rides:
            index-=1
        if index<=0:
            rides+=1
        else:
            pseats[maxIndex(pseats)]-=1
            pseats[index]+=1
    promos=0
    for i in range(len(seats)):
        promos+=max(0, pseats[i]-seats[i])
    print('Case #'+str(case)+':', rides, promos)
    #print(seats, pseats, rides)