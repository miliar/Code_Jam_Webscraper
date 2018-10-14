import math as mt
import itertools as it
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
def binarize(x,n): return  bin(x)[2:].zfill(n) #x - int, n - bits returns list
imp="IMPOSSIBLE"
pos="POSSIBLE"
inf=float('inf')
minf=(-1)*inf
pi=mt.pi
eps=10**(-9)
check_out=False
#check_out=True

f_in=open('in.in','r')
if (check_out):
    f_out = open('check.txt', 'w')
else:
    f_out=open('out.txt','w')


output=""
T=readint(f_in)

for test in range (T):
    output+="Case #"+str(test+1)+": "
    print "test: "+str(test+1)
    [n,c,m]=readint_l(f_in)
    cus=[[0 for i in range(n+1)]for i in range (c)]
    num=[0,0]
    for i in range(m):
        [p,b]=readint_l(f_in)
        cus[b-1][p-1]+=1
        num[b-1]+=1
    if (num[0]>num[1]):
        cus[1][n]=num[0]-num[1]
        num[1]=num[0]
    else:
        cus[0][n] = num[1] - num[0]
        num[0]=num[1]
    print cus

    if (cus[0][0]-sum(cus[1][1:])>=0):
        res=str(num[0]+cus[0][0]-sum(cus[1][1:]))+' '+str(0)
    else:
        ti=0
        for i in range(1,n):
            if (cus[0][i]>num[1]-cus[1][i]):
                ti=cus[0][i]-(num[1]-cus[1][i])
        res=str(num[0])+' '+str(ti)


    output+=res+"\n"

if (check_out):
    f_check=open('out.txt','r')
    right_str=f_check.read()
    print right_str==output


f_out.write(output)
f_out.close()
f_in.close()



