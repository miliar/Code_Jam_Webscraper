#!/usr/bin/env python


f1 = file('c-large-in.txt')

t = int(f1.readline())

for kk in range(1, t+1):
    n = int(f1.readline())
    
    s1 = (f1.readline()).split()
    a=[]
    for ax in s1:
       a.append(float(ax))
    a.sort()
#    for ax in a:
#        print ax
    s2 = (f1.readline()).split()
    b=[]
    for ax in s2:
       b.append(float(ax))
    b.sort()
#    for ax in b:
#        print ax
    
    aa= [1 for n in range(1, n+1)]
    bb= [1 for n in range(1, n+1)]
    
    retx = 0
    rety = 0
    
    for i in range(0,n):
        flag=0
        for j in range(0,n):
            if(a[i]<b[j])&(bb[j]==1):
                bb[j]=0
                flag = 1
                break
        if flag==0:
            rety=rety+1
            
    
    for i in range(0,n):
        flag=0
        for j in range(0,n):
            if(a[i]>b[j])&(aa[j]==1):
                aa[j]=0
                flag = 1
                retx = retx+1
                break
    
    
    print 'Case #'+str(kk)+': '+str(retx)+' '+str(rety)
