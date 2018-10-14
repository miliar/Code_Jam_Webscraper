
import math


def isemp(c1,n):
    for i in range(n):
        if c1[i]==[]:
            return 1
    return 0
def findmin(c2,n):
    res=c2[0][0]
    for i in range(n):
        if c2[i][0]<res:
            res=c2[i][0]
    return res


def delrow(c1,c2,n):
    for i in range(n):
        del c1[i][0]
        del c2[i][0]

def delmin(c1,c2,n,minin):
    for i in range(n):
        if c2[i][0]==minin:
            del c1[i][0]
            del c2[i][0]
def ok(c1,n,minin):
    for i in range(n):
        if c1[i][0]>minin:
            return 0
    return 1

g = open('output.txt', 'w')

f = open('B-large (1).in', 'r')

t= int(f.readline())
for i in range(t):
    s=f.readline().split()
    n=int(s[0])
    p=int(s[1])
    res=0
    r=[]
    q=[]
    s=f.readline().split()
    for j in range(n):
        r.append(int(s[j]))
    for j in range(n):
        s=f.readline().split()
        q.append([])
        for k in range(p):
            q[j].append(int(s[k]))
        q[j].sort()

    c1=[]
    c2=[]
    
    for j in range(n):
        c1.append([])
        c2.append([])
        for k in range(p):
            c1[j].append(math.ceil(q[j][k]/r[j]/1.1))
            c2[j].append(math.floor(q[j][k]/r[j]/0.9))
    while(isemp(c1,n)==0):
        minin=findmin(c2,n)
        if ok(c1,n,minin)==1:
            res=res+1
            delrow(c1,c2,n)
        else:
            delmin(c1,c2,n,minin)
    out="Case #" +str(i+1) +": "+str(res)+"\n"

    g.write(out)
g.close()
        

