#!/usr/bin/env python
# -*- coding: utf-8 -*-



if __name__ == "__main__":

    
    
    inFile = open("A-large.in","r")
    outFile = open("practice.out","w")
    
    caseNum = int(inFile.readline())

    for i in xrange(1,caseNum+1):
       
	N = int(inFile.readline())
	
	dzmap = []
	wp = {}
	owp = {}
	oowp = {}
	for j in xrange(N):
            tmp_str = inFile.readline().strip()
            
            dzmap.append(tmp_str)
            wp[j] = 0
            owp[j] = 0
            oowp[j] = 0
        for j in xrange(N):
            ttnum = 0
            ttwin = 0
            for k in xrange(N):
                if k == j or dzmap[j][k] == '.':
                    continue
                ttnum += 1
                if dzmap[j][k] == '1':
                    ttwin += 1
            if ttnum <> 0:
                wp[j] = float(ttwin) / float(ttnum)            
            
        for j in xrange(N):
            ttnum = 0
            ttwin = 0
            for k in xrange(N):
                if k == j or dzmap[j][k] == '.':
                    continue
                tmp_ttnum = 0
                tmp_ttwin = 0
                for g in xrange(N):
                    if g == j or dzmap[k][g] == '.':
                        continue
                    tmp_ttnum += 1
                    if dzmap[k][g] == '1':
                        tmp_ttwin += 1
                        
                if tmp_ttnum<> 0:
                    ttwin += float(tmp_ttwin) / float(tmp_ttnum)    
                ttnum += 1
                
            if ttnum<>0:
                owp[j] = float(ttwin) / float(ttnum)

        for j in xrange(N):
            ttnum = 0
            ttwin = 0
            for k in xrange(N):
                if k == j or dzmap[j][k] == '.':
                    continue
                ttnum += 1
                ttwin += owp[k]
            if ttnum<>0:
                oowp[j] = float(ttwin) / float(ttnum)
        if i>1:
            outFile.write("\n")
        outFile.write("Case #%d:" % (i,))
        for j in xrange(N):
            tmpnum = 0.25 *wp[j] + 0.50*owp[j] + 0.25*oowp[j]
            outFile.write("\n%.6f" % (tmpnum,))        
    outFile.close()
    inFile.close()
