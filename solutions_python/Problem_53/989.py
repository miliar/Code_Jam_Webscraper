#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

from __future__ import with_statement
import sys
import os

def compute(N, K):

    snappers = []
    for i in range(N):
        snappers.append(False)
    for j in range(K):
        for i in range(N):  
            if snappers[i] :
                snappers[i] = False
            else:
                snappers[i] = True
                break

    all_on = True  
    for i in range(N):
        if not snappers[i]:
            all_on = False
            break
    if all_on:
        return "ON"
    else:
        return "OFF"

with open(os.getcwd()+"/"+sys.argv[1], 'r') as fin:

    with open(os.getcwd()+"/output_"+sys.argv[1], 'w') as fout:

        C = int(fin.readline())
        for i in range(C):

            N, K = fin.readline().split()
            fout.write("Case #"+str(1+i)+": "+compute(int(N),int(K))+"\n")
