#!/usr/bin/env python
#coding=utf-8

"""
    Saving the Universe
"""

import math
#import sys

if __name__=='__main__':       

    #fin=open('A-small-attempt0.in','r')
    #fout=open('A-small-attempt0.out','w')
    fin=open('A-large.in','r')
    fout=open('A-large.out','w')
    
    seDict={}
    line=fin.readline()
    N=int(line.strip()) # Case count

    for i in range(N):
        case_id=i+1
        #print case_id
        seDict={}
        qrDict={}
        switches=0
        
        S=int(fin.readline().strip()) # Search Engines
        #print 'S',S        
        for j in range(S):
            seName=fin.readline().strip()
            seDict[seName]=1
            #print 'SE Name:',seName
            
        Q=int(fin.readline().strip()) # Query count
        #print 'Q',Q        
        for k in range(Q):
            query=fin.readline().strip()
            qrDict[query]=1
            #print 'Query:',len(qrDict)
            if len(qrDict)>=S:
                switches+=1
                qrDict.clear()
                qrDict[query]=1
                
        print 'Case #'+str(case_id)+': '+str(switches)
        fout.write('Case #'+str(case_id)+': '+str(switches)+'\n')
        
    fin.close()   
    fout.close()
    """
    line=fin.readline()
    S
    i=0
    newline=fin.readline()
    while i<n and newline:      
        i+=1
        variables=newline.split()
        num=variables[0]
        oldNSys=variables[1]
        newNSys=variables[2]
        newline=fin.readline()
        fout.write('Case #'+str(i)+': '+D2A(A2D(num,oldNSys),newNSys)+'\n')
    fin.close()
    fout.close()
    """
