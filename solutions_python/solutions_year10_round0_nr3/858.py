#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

from __future__ import with_statement
import sys
import os

def compute(R, k, N, gs):

    res = 0

    for i in range(R):

        seats = 0
        ins = []
        counter = 0
        while counter<N:
            num_people = gs.pop(0)
            seats+=num_people
            if(seats>k):
                gs.insert(0,num_people)
                break
            else:
                res+=num_people
                ins.append(num_people)
                counter+=1
        gs.extend(ins)

    return str(res)

with open(os.getcwd()+"/"+sys.argv[1], 'r') as fin:

    with open(os.getcwd()+"/output_"+sys.argv[1], 'w') as fout:

        T = int(fin.readline())
        for i in range(T):

            R, k, N = fin.readline().split()
            gs = [int(num) for num in fin.readline().split()]
            
            fout.write("Case #"+str(1+i)+": "+compute(int(R),int(k),int(N),gs)+"\n")
