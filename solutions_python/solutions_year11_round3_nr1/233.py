#!/usr/bin/env python
# -*- coding: utf-8 -*-



if __name__ == "__main__":

    
    
    inFile = open("A-large.in","r")
    outFile = open("practice.out","w")
    
    caseNum = int(inFile.readline())

    for i in xrange(1,caseNum+1):
        outFile.write("Case #%d:\n" % (i,))
        dzmap = []
	N,M = map(int,inFile.readline().strip().split())
	for k in xrange(N):
            tmp_str = inFile.readline().strip()
            dzmap.append([])
            for t in xrange(M):
                dzmap[k].append(tmp_str[t])
        pb = True
        for j in xrange(N):
            for g in xrange(M):
                if dzmap[j][g] == '.' or dzmap[j][g] == '\\' or dzmap[j][g] == '/':
                    continue
                if g ==M-1 or j == N-1 or dzmap[j][g+1] <> '#' or dzmap[j+1][g+1] <> '#' or dzmap[j+1][g] <> '#':
                    pb = False
                    break
                dzmap[j][g+1] = '\\'
                dzmap[j][g] = '/'
                dzmap[j+1][g] = '\\'
                dzmap[j+1][g+1] = '/'
            if not pb:
                break
        if not pb:
            outFile.write("Impossible\n")
        else:
            for j in xrange(N):
                for g in xrange(M):
     	            outFile.write(dzmap[j][g])
   	        outFile.write("\n")
   	        
    outFile.close()
    inFile.close()
