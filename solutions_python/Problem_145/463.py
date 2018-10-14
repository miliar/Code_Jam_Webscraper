#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Phenomics
#
# Created:     10/05/2014
# Copyright:   (c) Phenomics 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys
from math import log
from math import ceil

def gcc(a,b):
    if a<b: a,b=b,a;
    if a%b==0: return abs(b);
    return gcc(b,a%b)

def powerof2(c):
    while c>1:
        if c%2==0: c/=2
        else: return False;
    if c==1: return True;

with open('test_in.in','r') as f:
	data=f.readlines()

N=int(data[0]);
res="";
t=0;

for i in range(N):
    P,Q=[long(_) for _ in data[t+1].split('/')]
    t+=1;
    P,Q=(P/gcc(P,Q),Q/gcc(P,Q));
    if powerof2(Q):
        k=ceil(-log(P*1.0/Q,2));
        res_t=str(long(k))
    else: res_t="impossible"

    res+="Case #"+str(i+1)+": "+res_t +"\n"

with open('res.txt', 'w') as f:
	f.write(res)
