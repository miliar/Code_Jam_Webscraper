from __future__ import division

import os
import os.path, time
import itertools

def stalls(Line):
        arr=[int(x) for x  in Line.split()]
        s=arr[0]
        n=arr[1]
        print n
        arr=[s]
        for i in range(0,n-1):
                arr.append(int((arr[0]-1)/2))
                arr.append(arr[0]-1-int((arr[0]-1)/2))
                arr.pop(0)
                arr=sorted(arr,key=int, reverse=True)
        minim=int((arr[0]-1)/2)
        maxim=arr[0]-1-int((arr[0]-1)/2)

                

        
                
        return maxim,minim
        

        


#fo=open("test.txt")
#fw=open("test_out.txt","w")
fo=open("C-small-1-attempt0.in")
fw=open("C-small-1-attempt0.out","w")
#fo=open("B-large.in")
#fw=open("B-large.out","w")

n=int(fo.readline())
for k in range(0,n):
        Line=fo.readline().rstrip()
        
        print "Case #"+ str(k+1)+": "

        maxim,minim=stalls(Line)
        print stalls(Line)
        fw.write("Case #"+ str(k+1)+": ")
        fw.write(str(maxim)+" "+str(minim)+"\n")         
fw.close()        
        
                





