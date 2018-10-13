#!/usr/bin/env python

import random

random.seed()

raw_input()
raw_input()

print('Case #1:')

for i in range(0,100):
    data=[0 for i in range(0,6)]
    s=raw_input()
    l=[int(i) for i in s.split(' ')]
    pos=[0 for i in range(0,6)]
    for k in range(0,3):
        for j in range(0,7):
            x=l[j]
            if (x%2==0):
                pos[2]=1
                pos[4]=1
            if (x%3==0):
                pos[3]=1
            if (x%5==0):
                pos[5]=1
            if (x%5 == 0) & (data[5]<1):
                data[5]=1
            if (x%25 == 0) & (data[5]<2):
                data[5]=2
            if (x%125 == 0) & (data[5]<3):
                data[5]=3
                break
            if (x%3 == 0) & (data[3]<1):
                data[3]=1
            if (x%9 == 0) & (data[3]<2):
                data[3]=2
            if (x%27 == 0) & (data[3]<3):
                data[3]=3
                break
            if (x%64 == 0) & (data[4]<3):
                data[4]=3
                break
            if (x%32 == 0) & ((data[4]<2)&(data[2]<1)):
                data[4]=2
                data[2]=1
                break
            if (x%16 == 0):
                if (sum(data)>0) & (data[4]<2):
                    data[4]=2
            if (x%4==0) & (data[4]==0) & (data[2]==0) & (sum(data)==2):
                data[4]=1
                break
            if sum(data)==3:
                break
    s=''
    for i in range(0,data[2]):
        s+='2'
    for i in range(0,data[3]):
        s+='3'
    for i in range(0,data[4]):
        s+='4'
    for i in range(0,data[5]):
        s+='5'
    for i in range(0,(3-len(s))):
        pre=random.randint(2,5)
        if sum(pos)>0:
            while (pos[pre]==0):
                pre=random.randint(2,5)
        s+=str(pre)
    print(s)