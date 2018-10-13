t=int(input())
for t in range(t):
    x=input().split()
    n=int(x[1])
    st=x[0]
    pk=[]
    c=0
    for i in range(len(st)):
        if(st[i]=='+'):
            pk.append(1)
        else:
            pk.append(0)
    l=len(pk)
    for i in range(l-n):
        if(pk[i]==0):
            for j in range(i,i+n):
                pk[j]^=1
            c+=1
            i+=n
    s=0
    for i in range(l-n,l):
       s+=pk[i]
    print('Case #',end='')
    print(t+1,end=': ')
    if(s==n):
        print(c)
    elif(s==0):
        print(c+1)
    else:
        print('IMPOSSIBLE')
