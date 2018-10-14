#!/usr/bin/env python
# -*- coding: utf-8 -*-



if __name__ == "__main__":

    
    
    inFile = open("B-large.in","r")
    outFile = open("B.small.out","w")
    
    caseNum = int(inFile.readline())

    for i in xrange(1,caseNum+1):
        print i        
	tmplist = inFile.readline().split()
	comb_map = {}
        comb_num = int(tmplist[0])
        for j in xrange(1,comb_num+1):
            a,b,c = tmplist[j][0],tmplist[j][1],tmplist[j][2]
            if a not in comb_map:
                comb_map[a] = {}
            if b not in comb_map[a]:
                comb_map[a][b] = {}
            comb_map[a][b] = c

            if b not in comb_map:
                comb_map[b] = {}
            if a not in comb_map[b]:
                comb_map[b][a] = {}
            comb_map[b][a] = c
        
        oppo_map = {}
        oppo_num = int(tmplist[comb_num+1])
        for j in xrange(comb_num+2,comb_num+oppo_num+2):
            a,b = tmplist[j][0],tmplist[j][1]
            if a not in oppo_map:
                oppo_map[a] = {}
            if b not in oppo_map:
                oppo_map[b] = {}
            oppo_map[a][b] =1
            oppo_map[b][a] =1
            
        lng = int(tmplist[comb_num+oppo_num+2])
        test_str = tmplist[comb_num+oppo_num+3]
        left_str = ""
        
        for j in xrange(lng):
            c_char = test_str[j]

            if c_char in comb_map and len(left_str)>0 and left_str[-1] in comb_map[c_char]:
                
                tmpc = comb_map[c_char][left_str[-1]]
                left_str = left_str[:-1] + tmpc            
                continue
            
            if c_char in oppo_map:
                n = len(left_str) - 1
                while n>=0:
                    if left_str[n] in oppo_map[c_char]:
                        left_str = ""
                        break
                    n -= 1
                if n>=0:
                    continue

            
            
            
            left_str += c_char
                
        outFile.write("Case #%d: [" % (i,))
        for j in xrange(len(left_str)-1):
            outFile.write(left_str[j])
            outFile.write(", ")
        if len(left_str)>0:
            outFile.write(left_str[-1])
        outFile.write("]\n")

        
        
       
        
    outFile.close()
    inFile.close()
