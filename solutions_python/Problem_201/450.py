T = int(input())

for i in range(T):
    n,k = map(int, input().split())
    while k > 1:
        if n%2==0 and k%2==0:
            n2 = n//2
            k2 = k//2
        elif k%2==0:
            n2 = (n-1)//2
            k2 = k//2
        elif n%2==0:
            n2 = n//2 - 1
            k2 = (k-1)//2
        else:
            n2 = (n-1)//2
            k2 = (k-1)//2
        n,k = n2,k2
    print("Case #%d: %d %d"%(i+1,(n-1)//2+(n+1)%2,(n-1)//2))