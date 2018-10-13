# -*- coding: utf-8 -*-
"""
Created on Sun Apr 09 06:47:06 2017

@author: rajbhagat

For Code Jam - Faster Tidy numbers
"""

readfileopen=open("C:/Users/rajbh/Desktop/B-large.in",'r')
writefileout=open("C:/Users/rajbh/Desktop/B-large.out",'w')
caseno=0
for e in readfileopen:
    if caseno>0:
        
        checkno=int(e.strip().rstrip())
        ch=str(e.strip().rstrip())
        ls=list(ch)
        startno=0
        digiter=9
        noofdigits=len(ls)
        
        while startno<noofdigits:
            
            j=startno
            while j<noofdigits:
                ls[j]=digiter
                j+=1
            
            createdno=int("".join(str(x) for x in ls))
            ls=list(str(createdno))
            
            if createdno<=checkno:
                startno+=1
                digiter=9
            elif digiter!=1:
                digiter-=1
            else:
                noofdigits-=1
                startno=0
                digiter=9
                ls=ls[1:]
        
        outstring="Case #"+str(caseno)+": "+str(createdno)+"\n"
        
        writefileout.write(outstring)
    
    caseno+=1   

readfileopen.close()
writefileout.close()