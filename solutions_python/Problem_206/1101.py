t=int(input())
for test in range(t):
    d,n=map(int,input().split())
    mspeed=0
    for horse in range(n):
        k,s=map(int,input().split())
        mspeed=max(mspeed,(d-k)/s)
    print("Case #{}: {:.6f}".format(test+1,d/mspeed))
