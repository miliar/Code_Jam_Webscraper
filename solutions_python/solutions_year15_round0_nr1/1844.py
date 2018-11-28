tc=int(input())
for c in range(1,tc+1,1):
    sm,seated=input().split()
    sm=int(sm)
    p=0
    np=0
    for i in range(sm+1):
        if p-i<0:
            np+=(i-p)
            p+=(i-p)
        p+=int(seated[i])
    print("Case #{0}: {1}".format(c,np))

