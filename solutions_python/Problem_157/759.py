import os
import math
import copy
import sys
from collections import *
#import numpy as np

os.chdir('/Users/Dana/Downloads')
f = open('C-small-attempt0.in','r')
fo = open('C.out','w')
T = int(f.readline())
dic = {'i':1,'j':2,'k':3}
trans = [[0,1,2,3,4,5,6,7],
               [1,4,3,6,5,0,7,2],
               [2,7,4,1,6,3,0,5],
               [3,2,5,4,7,6,1,0],
               [4,5,6,7,0,1,2,3],
               [5,0,7,2,1,4,3,6],
               [6,3,0,5,2,7,4,1],
               [7,6,1,0,3,2,5,4]]
for ite in range(T):
    state = 0
    a,b = str.split(f.readline())
    a = int(a); b = int(b)
    c = list(f.readline())
    c = c[:len(c)-1]
    c = [dic[x] for x in c]
    c = c*b
    index = 0
    flag = True
    while state!=1 and flag:
        if (index<len(c)):
            state = trans[state][c[index]]
            index = index+1
        else:
            flag = False
    if flag:
        state = 0
        while state!=2 and flag:
            if (index<len(c)):
                state = trans[state][c[index]]
                index = index+1
            else:
                flag = False
    if flag:
        if index<len(c):
            state = 0
            for i in range(index,len(c)):
                state = trans[state][c[i]]
            if state!=3:
                flag = False
        else:
            flag = False
    print(ite)
    fo.write('Case #')
    fo.write(str(ite+1))
    fo.write(': ')
    if flag:
        fo.write('YES')
    else:
        fo.write('NO')
    fo.write('\n')
fo.close()

