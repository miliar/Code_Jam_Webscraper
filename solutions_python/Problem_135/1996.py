from math import *
import numpy as np


prob=(open('A-small-attempt0.in','r'))
#prob=(open('A-large.in','r')).read().split()
out=[]

T=int(prob.readline())


def solution():
    a1=int(prob.readline())-1
    b1=[[int(i) for i in prob.readline().split()] for _ in range(4)]
    a2=int(prob.readline())-1
    b2=[[int(i) for i in prob.readline().split()] for _ in range(4)]

    s1=set(b1[a1])
    s2=set(b2[a2])

    #print s1
    #print s2
    possible=list(s1 & s2) #intersection

    if len(possible)==0:
        return "Volunteer cheated!"
    elif len(possible)==1:
        return str(possible[0])
    else:
        return "Bad magician!"
    

for t in xrange(1,T+1):
    


    out.append("Case #%d: "%(t)+ solution())
    #print solution()


f=open('A-small.out','w')
#f=open('A-large.out','w')
f.write("\n".join(out))
f.close()
