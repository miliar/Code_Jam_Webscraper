# -*- coding: utf-8 -*-
"""
Created on Sun Apr 09 03:47:06 2017

@author: rajbhagat

For Code Jam - flipping Pan cakes
"""

readfileopen=open("C:/Users/rajbh/Desktop/A-large.in",'r')
writefileout=open("C:/Users/rajbh/Desktop/A-large.out",'w')
caseno=0
for e in readfileopen:
    if caseno>0:
        casecount=0
        req=e.strip().split(' ')
        pancakes=list(req[0])
        
        sizeno=int(req[1])
        pancakeno=0
        for pancake in pancakes:
            if pancake=='-' and pancakeno<=len(pancakes)-sizeno:
                pani=0
                while pani<sizeno:
                    
                    if pancakes[pancakeno+pani]=='-':
                        pancakes[pancakeno+pani]='+'
                    else:
                        pancakes[pancakeno+pani]='-'
                    
                    pani+=1
                
                casecount+=1
            
            pancakeno+=1
        
        res=str(casecount)+"\n"
        for e in pancakes:
            if e=='-':
                res="IMPOSSIBLE\n"
        outstring="Case #"+str(caseno)+": "+res
        
        writefileout.write(outstring)
    
    caseno+=1   

readfileopen.close()
writefileout.close()