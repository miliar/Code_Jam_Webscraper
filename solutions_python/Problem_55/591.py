import copy
import math
def rl(l, offset):
    if offset == 0:
        rv = copy.copy(l)
    else:
        real_offset = offset % int(math.copysign(len(l), offset))
        rv = (l[real_offset:] + l[:real_offset])
    return rv
def solve(r,k,n,grp):
    count=0
    sf=0
    prof=0
    for i in range(0,r):
        for x in grp:
            count=count+int(x)
            if count <= k:
                sf=sf+1
                prof=prof+int(x)
        grp=rl(grp,sf)
        count=0
        sf=0
    return prof

f=open('input','r')
fo=open('out','w')
x=-1
tli=[]
count=0
for line in f:
    if x==1:
        count=count+1
        fo.write("Case #" +str(count) +": " +str(solve(r,k,n,line.split()))
        +'\n')
        x=0
    elif x==0:
        tli=line.split()
        r=int(tli[0])
        k=int(tli[1])
        n=int(tli[2])
        x=1
    elif x==-1:
        T=int(line)
        x=0
