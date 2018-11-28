#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
Created on 2017/02/03

@author: 真吾
'''

def solve():

    m,K = fin.readline().split()
    K = int(K)
    m = list(m)
    count = 0

    def flip(m,i,K):
        for j in range(K):
            if m[i+j] == "+":
                m[i+j] = "-"
            else:
                m[i+j] = "+"
        return m

    for i in range(len(m)-K+1):
        if m[i] == "-" :
            m = flip(m,i,K)
            count = count + 1

    if "-" in m:
        count = "IMPOSSIBLE"


    return count

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

