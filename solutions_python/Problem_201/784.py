N = int(input())

for i in range(N):
    inp = list(map(int,input().split()))
    n,k = inp[0],inp[1]
    j = 1
    l = 1
    while(j<k and n>1):
        if n%2==1:
            l += j
        #else:
        #    l += j//2
        n = (n-1)//2+(n-1)%2
        k -= j
        j *= 2
#        print(n,k,j,l)

    if k<=l:
        ret = [(n-1)//2+(n-1)%2,(n-1)//2]
    else:
        ret = [(n-2)//2+(n-2)%2,(n-2)//2]
    if ret[1]<0:
        ret[1]=0

    print('Case #'+str(i+1)+': '+str(ret[0])+' '+str(ret[1]))
