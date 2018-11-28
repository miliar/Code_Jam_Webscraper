#!/usr/bin/python

#inf=open("input.txt")
#ouf=open("output.txt","w")
#inf=open("A-small-attempt0.in")
#ouf=open("A-small-attempt0.out","w")
inf=open("A-large.in")
ouf=open("A-large.out","w")


read=inf.readline
out=ouf.write

t=int(read())

def push(l,cost):
    pos=0
    global cnt
    for name in l:
        try:
            pos=dirs[pos][name]
        except:
            dirs[pos][name]=len(dirs)
            dirs.append({})
            cnt+=cost
            pos=dirs[pos][name]
            

for test in range(t):
    out('Case #%d: '%(test+1))
    n,m=map(int,read().split())
    dirs=[{}]
    cnt=0
    for i in range(n):
        push(read()[1:].strip().split('/'),0)
#    print dirs
    for i in range(m):
        push(read()[1:].strip().split('/'),1)
    out("%d\n"%cnt)
    print test
