from math import *
import numpy as np


#prob=(open('B-small-attempt0.in','r'))
prob=(open('B-large.in','r'))
out=[]

T=int(prob.readline())


def solution():
    C,F,X=(float(i) for i in prob.readline().split())

    curRate=2
    time=0

    while X/curRate > C/curRate+X/(curRate+F):
        time+=C/float(curRate)
        curRate+=F

    time+=X/curRate
    
    return str(time)
    

for t in xrange(1,T+1):
    


    out.append("Case #%d: "%(t)+ solution())
    #print solution()


#f=open('B-small.out','w')
f=open('B-large.out','w')
f.write("\n".join(out))
f.close()
