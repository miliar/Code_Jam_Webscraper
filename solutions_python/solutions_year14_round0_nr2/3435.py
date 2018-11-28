# -*- coding: utf-8 -*-
"""
Created on Sat Apr 12 16:43:22 2014

@author: ali
"""
f=open('input.txt','r')

def cookies(s):
    lt=s.split()
    C=float(lt[0])
    F=float(lt[1])
    X=float(lt[2])
    time=0
    if X<=C: 
        time=(X*1.0)/2
    elif X>C:
        k=0     
        while True:
            if (((X*1.0)/(2+k*F)) <= ((X*1.0)/(2+(k+1)*F) + (C*1.0/(2+k*F)))):
                time+=((X*1.0)/(2+k*F))
                break
            else:
                time+=((C*1.0)/(2+k*F))
                k=k+1
    return time

inputF=iter(f)
inputF.readline()

output=open('output.txt','w')

for N,s in enumerate(inputF,1):
    print >> output, "Case #%d: %f" % (N, cookies(s))

