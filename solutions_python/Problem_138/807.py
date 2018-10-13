# -*- coding: utf-8 -*-
"""
Created on Sat Apr 12 15:15:53 2014

@author: Matthieu
"""

fin = open("inputl.in","r")
fout = open("output.txt","w")
T = int(fin.readline())
ind = 1
while ind<T+1:
    N = int(fin.readline())
    wN = fin.readline().split()
    wN = [(float(k),0) for k in wN]

    wK = fin.readline().split()
    wK = [(float(k),1) for k in wK]
    
    w = wN + wK
    w.sort()
    
    decP = N
    compt = 0
    for i in range(2*N):
        if w[i][1]==0:
            if compt==0:
                decP-=1
            else:
                compt-=1
        else:
            compt+=1
    
    P = 0
    compt = 0
    for i in range(2*N-1,-1,-1):
        if w[i][1]==0:
            if compt==0:
                P+=1
            else:
                compt-=1
        else:
            compt+=1


    fout.write("Case #"+str(ind)+": ")
    fout.write(str(decP) + " " + str(P))
    fout.write("\n")
    ind+=1

fin.close()
fout.close()