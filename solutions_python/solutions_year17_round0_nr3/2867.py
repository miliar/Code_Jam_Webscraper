# -*- coding: utf-8 -*-
import sys

def findMinAndMaxBath(n,k,output):
    d =0
    tmp = k
    while(int(tmp/2) !=0):
        d = d+1
        tmp = int((tmp)/2)
    m = 2**(d)
    z=0
    if((n+1)%m > (k-m)):
        z= int((n+1)/m+1)
    else:
        z= int((n+1)/m)
    print(int((z-1)/2), int(z/2)-1)
    output.write(str(int((z-1)/2))+" " +str( int(z/2)-1)+"\n")
    

with open(sys.argv[1]) as f:
    with open(sys.argv[2],'w') as output:
        i = 1
        t = [int(x) for x in next(f).split()]
        for line in f: # read rest of lines
            n,m= [int(x) for x in line.split()]
            output.write("Case #"+ str(i)+": ")
            i=i+1
            findMinAndMaxBath(n,m,output)



