#!/usr/bin/env python
# -*- coding: utf-8 -*-



if __name__ == "__main__":
    
    inFile = open("A-large.in","r")
    outFile = open("practice.out","w")
    
           
        
    caseNum = int(inFile.readline())
    for i in xrange(1,caseNum+1):
        rtv = 0
        N,M = tuple(map(int,inFile.readline().strip().split()))

        dlist = {}
        for _ in range(N):
            tmp_map = inFile.readline().strip().split("/")
            tmp_l = dlist
            for items in tmp_map:
                if len(items) == 0:
                    continue
                if items not in tmp_l:
                    tmp_l[items] = {}
                tmp_l = tmp_l[items]
        
        for _ in range(M):
            tmp_map = inFile.readline().strip().split("/")
            tmp_l = dlist
            for items in tmp_map:
                if len(items) == 0:
                    continue
                if items not in tmp_l:                    
                    rtv += 1
                    tmp_l[items] = {}
                tmp_l = tmp_l[items]
        outFile.write("Case #%d: %d\n" % (i,rtv))
    outFile.close()
    inFile.close()
