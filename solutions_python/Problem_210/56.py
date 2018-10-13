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
check_out=False
#check_out=True

f_in=open('in.in','r')
if (check_out):
    f_out = open('check.txt', 'w')
else:
    f_out=open('out.txt','w')

def find_swaps(li,a):
    li.sort()
    leng=len(li)
    for i in range(leng):
        if (sum(li[:i+1])>720-a):
            return leng-i

output=""
T=readint(f_in)


for test in range (T):
    output+="Case #"+str(test+1)+": "
    print (test+1)

    [ac,aj]=readint_l(f_in)
    cint=[]
    jint=[]
    cwork=0
    jwork=0
    for i in range(ac):
        cint.append(readint_l(f_in)+[0])
        cwork+=cint[i][1]-cint[i][0]
    for i in range(aj):
        jint.append(readint_l(f_in)+[1])
        jwork += jint[i][1] - jint[i][0]
    allwork=cint+jint
    allwork.sort(key=lambda x:x[0])
    miss=[[],[]]
    summiss=[0,0]
    must=0
    prev=0
    for i in range(ac+aj+1):
        if i == ac + aj:
            curr = allwork[0]
            curr[0]+=24*60
        else:
            curr=allwork[i]
        if i==0:
            prev=curr
            continue


        if (prev[2]==curr[2]):
            miss[curr[2]].append(curr[0]-prev[1])
            summiss[curr[2]]+=curr[0]-prev[1]
        else:
            must+=1
        prev=curr
    if (cwork+summiss[0]>720):
        must+=2*find_swaps(miss[0],cwork)
    else:
        if (jwork+summiss[1]>720):
            must += 2 * find_swaps(miss[1],jwork)


    ans=max(2,must)

    output+=str(ans)+"\n"

if (check_out):
    f_check=open('out.txt','r')
    right_str=f_check.read()
    print right_str==output


f_out.write(output)
f_out.close()
f_in.close()



