
t = int(input())

for i in range(1, t+1):
    
    d, n = [int(x) for x in input().split()]
    
    t = 0
    
    for j in range(n):
        k, s = [int(x) for x in input().split()]
        
        t = max(t, (d-k)/s)
    
    speed = d / t
        
    print("Case #{}: {}".format(i, speed))