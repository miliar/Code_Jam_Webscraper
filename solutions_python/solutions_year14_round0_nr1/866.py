# -*- coding: utf-8 -*-
"""
Created on Sat Apr 12 11:59:10 2014

@author: Matthieu
"""

fin = open("input.in","r")
fout = open("output.txt","w")
T = int(fin.readline())
ind = 1
while ind<T+1:
    ans1 = int(fin.readline())
    for i in range(1,5):
        if i == ans1:
            line = fin.readline()
            line = line.split()
            line = [int(k) for k in line]
        else:
            fin.readline()
    ans2 = int(fin.readline())
    for i in range(1,5):
        if i == ans2:
            line2 = fin.readline()
            line2 = line2.split()
            line2 = [int(k) for k in line2]  
        else:
            fin.readline()
    res = [i for i in line if i in line2]
    print res
    fout.write("Case #"+str(ind)+": ")
    if(len(res)==0):
        fout.write("Volunteer cheated!")
    elif(len(res)>1):
        fout.write("Bad magician!")
    else:
        fout.write(str(res[0]))
    fout.write("\n")
    ind+=1

fin.close()
fout.close()