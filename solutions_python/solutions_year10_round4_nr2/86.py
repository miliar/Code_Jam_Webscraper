#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime


if __name__ == "__main__":
    
    inFile = open("B-small-attempt0.in","r")
    outFile = open("practice_B_L.out","w")
    print datetime.datetime.now()
           
        
    caseNum = int(inFile.readline())
    for i in xrange(1,caseNum+1):
        
        P = int(inFile.readline().strip())
        ml = map(int,inFile.readline().strip().split())
        pl = []
        rtvl = []
        for _ in range(P):
            pl.append(map(int,inFile.readline().strip().split()))
            rtvl.append([0 for _ in range(2**P)] )

        
            
        for tt in xrange(2**P):
            tmp_c = tt
            cnt = 0            
            while cnt<P-ml[tt]:                
                rtvl[P-cnt-1][tt/(2**(P-cnt))] = 1
                
                cnt +=1
        rtv = 0
        for h in range(P):
            for t in xrange(2**(P-1-h)):
                if  rtvl[h][t] == 1:
                    rtv += pl[h][t]

        
        outFile.write("Case #%d: %d\n" % (i,rtv))
    
    outFile.close()
    inFile.close()
