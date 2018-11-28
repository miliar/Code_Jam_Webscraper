import os
import math
import copy
import sys
import numpy as np

os.chdir('C:/Python33/20141B')
f = open('A-small-attempt0.in','r')
fo = open('A-small.out','w')
#f = open('B-large.in','r')
#fo = open('B-large.out','w')
T = int(f.readline())
for ite in range(T):
    fo.write('Case #')
    fo.write(str(ite+1))
    fo.write(': ')
    N = int(f.readline())
    #zm = np.matrix([' ' for i in range(100*N)]).reshape(N, 100)
    #cs = np.matrix([0 for i in range(100*N)]).reshape(N,100)
    zm = ['abc']*N
    letter = [[' ' for i in range(100)] for j in range(N)]
    times = [[0 for i in range(100)] for j in range(N)]
    for i in range(N):
        zm[i] = f.readline()
        zm[i] = zm[i][:len(zm[i])-1]
        temp = zm[i][0]
        letter[i][0] = temp
        times[i][0] = 1
        index = 0
        for j in range(1,len(zm[i])):
            if zm[i][j] == temp:
                times[i][index] = times[i][index]+1
            else:
                temp = zm[i][j]
                index = index+1
                letter[i][index] = temp
                times[i][index] = 1
    #print(letter)
    #print(times)
    index = index+1  # index letters
    flag = 1
    for i in range(1,N):
        if not letter[i]==letter[0]:
            flag = 0
    if flag==0:
        fo.write('Fegla Won')
    else:
        s = 0
        for j in range(index):
            middle = sum(times[i][j] for i in range(N))/N
            s1 = 0
            s2 = 0
            m1 = math.floor(middle)
            m2 = math.ceil(middle)
            for i in range(N):
                s1 = s1 + abs(times[i][j]-m1)
                s2 = s2 + abs(times[i][j]-m2)
            if s1<s2:
                s = s+s1
            else:
                s = s+s2
        fo.write(str(s))
    print(ite)
        
    fo.write('\n')
fo.close()

