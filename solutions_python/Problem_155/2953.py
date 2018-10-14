# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 00:30:42 2015

@author: Taras
"""

import math

f = open('C:\study\gjam\\A-large.in')
f_out = open('C:\\study\\gjam\\res.txt','w+')
num_test = int(f.readline())




for t in range(num_test):      

       

    max_sil, inp_seq = f.readline().split()
    max_sil = int(max_sil)
    inp_seq = list(inp_seq)
    inp_seq = [int(x) for x in inp_seq]
    
    num_friends  = 0
    num_standing = 0
    
    for k in range(len(inp_seq)):
        if (num_standing < k):
            num_friends = num_friends + (k - num_standing)
            num_standing = k
        num_standing = num_standing + inp_seq[k]

        
        


    f_out.write("Case #"+str(t+1)+": ")       
    f_out.write(str(num_friends) + '\n')
    #f.readline()


f.close()
f_out.close()
