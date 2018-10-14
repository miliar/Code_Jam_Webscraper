gi=int(input())
#take the test cases
for gi in range(gi):
    #takes the va;ues
    xi=input().split()
    n=int(xi[1])
    f=[]
    #initialising the variables
    k=0
    k=k+1
    ij=k%10
    c=0
    gkl=ij/15
    #for loop
    for i in range(len(xi[0])):
        if(xi[0][i]=='+'):
            f.append(1)
            gkl=gkl+1
        else:
            f.append(0)
    l=len(f)
    ddy=l
    #for loop 
    for i in range(l-n):
        if(f[i]==0):
            for j in range(i,i+n):
                f[j]^=1
            c+=1
            klm=k%9
            i+=n
    summ=0
    # taking the sum
    for i in range(l-n,l):
       summ+=f[i]
    print('Case',end=' ')
    print('#',end='')
    print(gi+1,end=': ')
    if(klm==k):
        k=0
    if(summ==n):
        print(c)
    elif(summ==0):
        print(c+1)
    else:
        print('IMPOSSIBLE')
