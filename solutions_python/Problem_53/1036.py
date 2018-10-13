#Dan Test

import string

file1=r"d:\Download Firefox\A-small-attempt2.in"
output=r"d:\Download Firefox\A-small-attempt2.out"


def solve(n, k, nr):
    list2=[]
    for i in range(n):
        list2.append(0)
    poz=0
    for  j in range(k):
        poz=0
        for c in range(n):
            if list2[c]==1:
                poz=c+1
            else:
                break
        if poz>n-1:
            poz=n-1
        
        for elem in range(poz+1):
            if list2[elem]==1:
                list2[elem]=0
            else:
                list2[elem]=1

        poz=0
        
        for c in range(n):
            if list2[c]==1:
                poz=c+1
            else:
                break
        if poz>n-1:
            poz=n-1        
        
    if (poz==(n-1)) and (list2[n-1]==1):
        s="ON"
        g.write('Case #%d: %s\n'% (nr,s))
    else:
        s="OFF"
        g.write('Case #%d: %s\n'% (nr,s))
          

f=open(file1,'r')
g=open(output,'w')
aux=f.readline().rstrip('\n')
tc=int(aux)
for i in range(1, tc+1):
    line=f.readline().rstrip('\n') #read N, K
    list1=line.split(' ')
    n=int(list1[0])
    k=int(list1[1])
    solve(n,k,i)
          
                        
f.close()
g.close()


    
