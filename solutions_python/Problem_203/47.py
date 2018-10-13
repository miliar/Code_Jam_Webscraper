import math
fin=open("ac.in","r")
fout=open("ac.out","w")
T=int(fin.readline().strip())
def f(S):
    M=list(S)
    x=0
    while M[x]=='?':
        x+=1
    for y in range(x):
        M[y]=M[x]
    c=M[x]
    start=x+1
    while start<len(M):
        if M[start]=='?':
            M[start]=c
        else:
            c=M[start]
        start+=1
    return M
for dummy in range(T):
    print dummy+1
    if dummy>0:
        fout.write('\n')
    fout.write("Case #"+str(dummy+1)+": ")
    [R,C]=[int(x) for x in fin.readline().split()]
    A=[['?' for x in range(C)]for y in range(R)]
    for dummy2 in range(R):
        A[dummy2]=list(fin.readline().strip())
    print A
    TR=['?'for x in range(R)]
    TC=['?'for x in range(C)]
    start=0
    while A[start]==TC:
        start+=1
    A[start]=f(A[start])
    for x in range(start):
        A[x]=A[start]
    start+=1
    while start<R:
        if A[start]==TC:
            A[start]=A[start-1]
        else:
            A[start]=f(A[start])
        start+=1
    for v in range(R):
        fout.write('\n')
        for u in range(C):
            fout.write(A[v][u])
        
