# -*- coding: utf-8 -*-
"""
Created on Sat Apr 12 13:08:47 2014

@author: Matthieu
"""

fin = open("inputl.in","r")
fout = open("output.txt","w")
T = int(fin.readline())
ind = 1
while ind<T+1:
    line = fin.readline()
    line = line.split()
    line = [float(k) for k in line]
    C = line[0]
    F = line[1]
    X = line[2]
    time = 0
    f = 2
    while C/f+X/(f+F)<X/f:
        time += C/f
        f+=F
    time += X/f
    fout.write("Case #"+str(ind)+": ")
    fout.write(str(time))
    fout.write("\n")
    ind+=1

fin.close()
fout.close()