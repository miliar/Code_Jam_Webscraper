#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

fin = open('snapper.in','r')
fout = open('snapper.out','w')
T = int(fin.readline())
for t in range(T):
    N,K = [int(i) for i in fin.readline().split()]
    if (K+1)%(2**N) == 0:
        fout.write("Case #"+str(t+1)+": ON\n")
    else:
        fout.write("Case #"+str(t+1)+": OFF\n")
fout.close()
fin.close()
