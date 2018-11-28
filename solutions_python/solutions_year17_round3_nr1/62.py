import math as mt
import numpy as np
import heapq as hq


def readint(f_in): return int(f_in.readline()[:-1])
def readfloat(f_in): return float(f_in.readline()[:-1])
def read_l(f_in): return f_in.readline()[:-1].split(' ')
def readint_l(f_in): return map(int,f_in.readline()[:-1].split(' '))
def readfloat_l(f_in): return map(float,f_in.readline()[:-1].split(' '))
def readchar_l(f_in): return list(f_in.readline()[:-1])
def plus_min_str_to10_l(str): return map(int,list(str.replace('+','1').replace('-','0')))
def list_to_str(out_list): return ' '.join(map(str,out_list))
imp="IMPOSSIBLE"
pos="POSSIBLE"
inf=float('inf')
minf=(-1)*inf
pi=mt.pi
check_out=False
#check_out=True

f_in=open('in.in','r')
if (check_out):
    f_out = open('check.txt', 'w')
else:
    f_out=open('out.txt','w')

def find_sum(li,leng,am):
    so=sorted(li,key=lambda x:x[1]*x[0])
    sumi=0
    for i in range(leng-am,leng):
        sumi+=so[i][1]*so[i][0]
    return sumi

output=""
T=readint(f_in)

for test in range (T):
    output+="Case #"+str(test+1)+": "
    print (test+1)

    [n,k]=readint_l(f_in)
    li=[]
    for i in range (n):
        li.append(readint_l(f_in))
    li.sort(key=lambda x:x[0])
    maxi=minf
    for i in range(k-1,n):
        this_max=(pi*li[i][0]**2)+2*pi*(li[i][0]*li[i][1]+find_sum(li[:i],i,k-1))
        maxi=max(maxi,this_max)

    output+=str(maxi)+"\n"

if (check_out):
    f_check=open('out.txt','r')
    right_str=f_check.read()
    print right_str==output


f_out.write(output)
f_out.close()
f_in.close()



