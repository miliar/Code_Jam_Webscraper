#!/usr/bin/env python
# -*- coding: utf-8 -*-


if __name__ == "__main__":

    
    
    inFile = open("C-small-attempt1.in","r")
    outFile = open("practice.out","w")
    
    caseNum = int(inFile.readline())

    for i in xrange(1,caseNum+1):          
	N,L,H = map(int,inFile.readline().strip().split())
	dzmap = map(int,inFile.readline().strip().split())
	
	fi = False
	for j in xrange(L,H+1):
            tf = True
            for item in dzmap:
                
                if j%item>0 and item%j>0:
                    tf = False
                    break
            if tf:
                outFile.write("Case #%d: %d\n" % (i,j))
                fi = True
                break
        if not fi:
            outFile.write("Case #%d: NO\n" % (i,))
            
        
   	        
    outFile.close()
    inFile.close()
