#!/usr/bin/env python
#coding=utf-8
"""
    Round 1A
"""

if __name__=="__main__":
    fin=open('A-large.in','r')
    fout=open('A-large.out','w')
    
    X=[]
    Y=[]
    
    line=fin.readline()
    T=int(line.strip()) # Case count
    #print T
    for i in range(T):
        X=[]
        Y=[]
        d=int(fin.readline().strip())
        #print d
        Xstr=fin.readline().strip().split()
        Ystr=fin.readline().strip().split()
        for k in range(d):
            X.append(int(Xstr[k]))
            Y.append(int(Ystr[k]))
        X.sort()
        Y.sort()
        #print X
        #print Y
        min_scalar_product=0
        for j in range(d):
            min_scalar_product+=X[j]*Y[d-j-1]
            
        print 'Case #'+str(i+1)+': '+str(min_scalar_product)
        fout.write('Case #'+str(i+1)+': '+str(min_scalar_product)+'\n')
    fin.close()
    #fout.close()
