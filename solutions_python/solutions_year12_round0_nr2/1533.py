#!/usr/bin/python

a=open("dance_googlers.txt","r")
f=a.read()
a.close()
f=f.split('\n')

T=int(f[0])
for i in range(1,len(f)):
    f[i]=f[i].split()
cs=0
a=open("Output.txt","w+")
for i in f[1:]:
    N=int(i[0])
    S=int(i[1])
    P=int(i[2])
    fu=[]
    for j in range(N):
      fu.append(int(i[j+3]))
    p1=3*P-4
    p2=3*P-3
    sd=1
    if p1<0 or p2<0:
        if p1<0:
            p1=P
        if p2<0:
            p2=P
        sd=0
    cou=0
    for k in fu:
        if k>=p1:
            if k==p1 or k==p2:
                if S!=0:
                    S-=1
                    cou+=1
                    continue
                elif sd==0:
                    cou+=1
                    continue
            else:
                cou+=1

    cs+=1
    st="Case #"+str(cs)+': '+str(cou)+"\n"
    a.write(st)
a.close()
