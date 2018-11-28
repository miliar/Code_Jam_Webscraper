#!/usr/bin/env python
# -*- coding: utf-8 -*-



if __name__ == "__main__":

    
    
    inFile = open("C-large.in","r")
    outFile = open("C-large.out","w")
    
    caseNum = int(inFile.readline())

    for i in xrange(1,caseNum+1):
        print i
        pileNum = int(inFile.readline())
	tmplist = sorted(map(int,inFile.readline().split()))
	a = 0
	sumall = 0
	for item in tmplist:
            a = a^item
            sumall += item        
        if a ==0:
            sumall -= tmplist[0]
            outFile.write("Case #%s: %d\n" % (i,sumall))
        else:
            outFile.write("Case #%s: NO\n" % (i,))

        
        
       
        
    outFile.close()
    inFile.close()
