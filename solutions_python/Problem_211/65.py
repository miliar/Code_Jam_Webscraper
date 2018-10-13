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


output=""
T=readint(f_in)

for test in range (T):
    output+="Case #"+str(test+1)+": "
    print (test+1)

    [n,k]=readint_l(f_in)
    u= readfloat(f_in)
    prob=readfloat_l(f_in)

    prob.sort()
    if (test+1==46):
        print prob
        print u
    x=0
    while(u>0 and x<100):
        x+=1
        mini=prob[0]
        ind=1
        if (prob[n-1]==mini):
            ind=n
            upto=1.0
        else:
            while(prob[ind]==mini):
                ind+=1
            upto=prob[ind]

        if (u>=ind*(upto-mini)):
            for i in range(ind):
                prob[i]=upto
            u-=ind*(upto-mini)
            print u
        else:
            for i in range(ind):
                prob[i]+=u/ind
            u=0
    if (test+1==46):
        print prob
        print u
    ans=reduce(lambda x,y: x*y, prob)




    output+=str(ans)+"\n"

if (check_out):
    f_check=open('out.txt','r')
    right_str=f_check.read()
    print right_str==output


f_out.write(output)
f_out.close()
f_in.close()



