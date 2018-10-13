T = int(input())

for i in range(1, T+1):
    
    N, K = [int(x) for x in input().split()]
    u = float(input())
    P = [float(x) for x in input().split()]
    
    P.sort()
    P.append(1.0)
    
    fp = 1
    for j in range(N):
        if u >= (j+1) * (P[j+1] - P[j]):
            u = u - (j+1) * (P[j+1] - P[j])
        else:
            fp = P[j] + u / (j + 1)
            break
    
    y = fp ** (j + 1)
    for p in P[j+1:]:
        y = y * p
    
    print("Case #{}: {}".format(i, y))