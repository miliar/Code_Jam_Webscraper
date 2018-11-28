from __future__ import division

import os
import os.path, time
import itertools

def flip(x,Line_bin):
        start=len(Line_bin)
        for i in range(0,len(Line_bin)):
                if Line_bin[i]==0:
                        start=i
                        break
        arr_start=Line_bin[:start]
        arr_flip=Line_bin[start:start+x]
        arr_rest=Line_bin[start+x:]
        arr_flip=[abs(i-1) for i in arr_flip]
        return start+x,(arr_start+arr_flip+arr_rest)

def combine(Line_bin):
        Sumline=0
        for i in range (0,len(Line_bin)):
                Sumline=Sumline+Line_bin[i]
        Sum=Sumline/len(Line_bin)
        return(Sum)
                
                
        

def numflips(Line_all):
        Line_bin=[]
        Line,fn=Line_all.split()
        Line_arr=[i for i in str(Line)]
        for i in range(0,len(Line_arr)):
                if Line_arr[i]=="+":
                        Line_bin.append(1)
                elif Line_arr[i]=="-":
                        Line_bin.append(0)
        flipnum=int(fn)
        simple=combine(Line_bin)
        flips=0
        s=0
        while simple!=1.0:
                s,Line_bin=flip(flipnum,Line_bin)
                simple=combine(Line_bin)
                flips=flips+1
        if s>len(Line_bin):
                return "IMPOSSIBLE"
        else:
                return(flips)
        
        


#fo=open("test.txt")
#fw=open("test_out.txt","w")
#fo=open("A-small-attempt0.in")
#fw=open("A-small-attempt0.out","w")
fo=open("A-large.in")
fw=open("A-large.out","w")

n=int(fo.readline())
for k in range(0,n):
        Line=fo.readline()

        print "Case #"+ str(k+1)+": "
        print(numflips(Line))
        fw.write("Case #"+ str(k+1)+": ")
        fw.write(str(numflips(Line))+"\n")         
fw.close()        
        
                





