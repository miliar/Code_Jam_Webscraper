import math

t = int(input())

for i in range(1, t + 1):
    n, k = [int(x) for x in input().split()]
    res = 0    
    S = []
    H = []
    
    for j in range(n):
        r, h = [int(x) for x in input().split()]
        S.append((r ** 2, 2 * r * h, j))
        H.append((2 * r * h, r ** 2, j))
    
    S.sort(reverse = True)
    H.sort(reverse = True)
    
    seen = []
    
    for j in range(n - k + 1):
        s = S[j][0] + S[j][1]
        
        seen.append(S[j][2])
        
        count = k - 1
        for h in H:
            if count == 0:
                break
            
            if h[2] not in seen:
                s = s + h[0]
                count = count - 1
                
        if count <= 0 :
            res = max(s, res)
    
    print("Case #{}: {}".format(i, res * math.pi))