#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
Created on 2017/02/03

@author: 真吾
'''

def solve():

    N = list(fin.readline().replace('\n',''))
    ans1=0
    flag = True
    while(flag):
        flag = False
        for i in range(len(N)-1):
            if int(N[i]) > int(N[i+1]):
                flag = True
                N[i] = int(N[i]) -1
                for j in range(len(N)-i-1):
                    N[j+i+1] = 9

    for i in range(len(N)):
        N[i] = str(N[i])
    ans1=int(''.join(N))
    return ans1

import time
start = time.time()
print("Started!")
fin = open('in.txt', 'rt')
fout=open("out.txt", 'wt')

T = int(fin.readline())
for i in range(T):
    #print('Now Case {}'.format(i+1))
    fout.write('Case #{}: {}\r\n'.format(i+1, solve()))
fout.close()
print("finished!")
elapsed_time = time.time() - start
print (("elapsed_time:{0}".format(elapsed_time)) + "[sec]")

