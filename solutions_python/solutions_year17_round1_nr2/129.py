
t = int(input())
for i in range(1, t+1):
    Q = {}
    count = 0
    good = True
    
    N, P = [int(x) for x in input().split()]
    
    R = [int(x) for x in input().split()]
    
    for j in range(N):
        Q[j] = sorted([int(x)/R[j] for x in input().split()])
    
    l = [Q[j].pop(0) for j in range(N)]
    m = 1
    while good: 
        while all([l[j] >= 0.9 * m for j in range(N)]):
            if all([l[j] <= 1.1 * m for j in range(N)]):
                try:
                    l = [Q[j].pop(0) for j in range(N)]
                except:
                    good = False
                count = count + 1
                m = 1
                break
            else:
                m = m + 1
        
        else:
            for j in range(N):
                if l[j] >= 0.9 * m:
                    continue
                while Q[j]:
                    l[j] = Q[j].pop(0)
                    if l[j] >= 0.9 * m:
                        break
                else:
                    good = False
                    break   
                 
        
    print("Case #{}: {}".format(i, count))