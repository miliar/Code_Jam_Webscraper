def do():
    N,K = map(int, input().split())
    U = float(input())
    P = [float(x) for x in input().split()]

    P.sort()
    P.append(1.0)

    prob = 0
    
    i = 0
    while i < N:
        cost = (i+1)*(P[i+1] - P[i])
        if cost-0.000001 <= U:
            U -= cost
            i += 1
        else:
            break
    prob = (P[i] + U/(i+1))**(i+1)

    for j in range(i+1,N):
        prob *= P[j]
            
    return prob
        
        

t = int(input())

for _ in range(t):
    print(f'Case #{_+1}: {do():.10f}')
