#!/usr/bin/python3
# -*- coding: utf8 -*-

fin = open("input.txt",'r')
fout = open("output.txt",'w')
n = int(fin.readline())
for i in range(n):
    n,k = map(int,fin.readline().split())
    s = "ON" if (k+1)%(2**n)==0 else "OFF"
    print ("Case #%d: %s"%(i+1,s),file=fout)
