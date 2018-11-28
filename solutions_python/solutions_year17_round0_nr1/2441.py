g=int(input())
for g in range(g):
    x=input().split()
    n=int(x[1])
    pf=[]
    c=0
    for i in range(len(x[0])):
        if(x[0][i]=='+'):
            pf.append(1)
        else:
            pf.append(0)
    l=len(pf)
    for i in range(l-n):
        if(pf[i]==0):
            for j in range(i,i+n):
                pf[j]^=1
            c+=1
            i+=n
    su=0
    for i in range(l-n,l):
       su+=pf[i]
    print('Case',end=' ')
    print('#',end='')
    print(g+1,end=': ')
    if(su==n):
        print(c)
    elif(su==0):
        print(c+1)
    else:
        print('IMPOSSIBLE')
