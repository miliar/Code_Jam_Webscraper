#!/usr/bin/env python
# -*- coding: utf-8 -*-



if __name__ == "__main__":

    
    
    inFile = open("A-large.in","r")
    outFile = open("practice.out","w")
    
    caseNum = int(inFile.readline())

    for i in xrange(1,caseNum+1):
        print i
        maplist = {"O":[],"B":[]}
	tmplist = inFile.readline().split()
        stepnum = int(tmplist[0])
        
        for j in xrange(stepnum):
	    maplist[tmplist[j*2+1]].append((int(tmplist[j*2+2]),j))
	
	op_i = 0
	bp_i = 0
	op = 1
	bp = 1
	
	totalstep = 0
	while op_i < len(maplist["O"]) or bp_i < len(maplist["B"]):
            
            if op_i == len(maplist["O"]):
                btarget, bi = maplist["B"][bp_i]                
                totalstep += abs(btarget - bp) + 1
                bp = btarget
                bp_i += 1
                continue
            if bp_i == len(maplist["B"]):
                otarget, oi = maplist["O"][op_i] 
                totalstep += abs(otarget - op) + 1
                op = otarget
                op_i += 1
                continue
            
            costep = 0
            cbstep = 0
            
            btarget, bi = maplist["B"][bp_i]
            otarget, oi = maplist["O"][op_i]            
            
            costep = abs(otarget - op)                
            cbstep = abs(btarget - bp)

            if bi<oi:
                totalstep += cbstep + 1
                bp = btarget
                bp_i += 1
                if costep > cbstep:
                    if otarget < op:
                        op = op - cbstep - 1
                    else:                    
                        op = op + cbstep + 1
                else:
                    op = otarget
            else:
                totalstep += costep + 1
                op = otarget
                op_i += 1
                if cbstep > costep:
                    if btarget < bp:
                        bp = bp - costep - 1
                    else:                    
                        bp = bp + costep + 1
                else:
                    bp = btarget
                
            
            
            
           
           
                
        outFile.write("Case #%d: %s\n" % (i,totalstep))
        
        
       
        
    outFile.close()
    inFile.close()
