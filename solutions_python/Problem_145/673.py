## PArt elf problem
## Solution program code

import math
import numpy

def power(n):
    r=0
    while n//2==n/2:
        r+=1
        n=n//2
    return(r,n)

def power2(n):
    r=0
    while n/2>1:
        r+=1
        n=n/2
    return(r)

f=open("A-small-attempt0.in")
input_lines=f.read().splitlines()
f.close

input_lines2=[]
for line in input_lines:
    input_lines2.append([int(s) for s in line.split('/')])




T=int(input_lines2[0][0])
g = open("output.out", 'w')
for i in range(T):
    P=int(input_lines2[i+1][0])
    Q=int(input_lines2[i+1][1])
    p2=power(P)
    q2=power(Q)
    if p2[1]/q2[1]!=p2[1]//q2[1] or P/Q<1/(2**40):
        g.write('Case #'+str(i+1)+': Impossible\n')
    else:
        if p2[0]>q2[0]:
            P2=P//(q2[1]*(2**q2[0]))
            Q2=Q//(q2[1]*(2**q2[0]))
        else:
            P2=P//(q2[1]*(2**p2[0]))
            Q2=Q//(q2[1]*(2**p2[0]))
        answer=str(power(Q2)[0]-power2(P2))
        g.write('Case #'+str(i+1)+': '+answer+'\n')

g.close()





