#!/usr/bin/env python
# -*- coding: utf-8 -*-



if __name__ == "__main__":

    
    
    inFile = open("D-large.in","r")
    outFile = open("D-large.out","w")
    
    caseNum = int(inFile.readline())

    for i in xrange(1,caseNum+1):
        N = int(inFile.readline())
	tmplist = map(int,inFile.readline().split())	
        for j in xrange(1,len(tmplist)+1):
            if j == tmplist[j-1]:
                N -= 1
        outFile.write("Case #%d: %.6f\n" % (i,N))
        
        
       
        
    outFile.close()
    inFile.close()
