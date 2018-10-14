tt = int(input())
for case in range(1, tt+1):
    d,n = list(map(int, input().split()))
    h = list()
    go = 0.0
    for i in range(n):
        k,m = list(map(float, input().split())) 
        if d >= k:
            go = max(go, (d-k)/m) 
    print("Case #%d: %f"%(case, d/go))
