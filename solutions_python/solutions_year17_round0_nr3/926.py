

def add_to_list(G, x, M):
    for i, xM in enumerate(G):
        if M == xM[1]:
            xM[0] += x
            break
    else:
        G.append([x,M])
        G.sort(key=lambda x: x[1])

T = int(input())

for t in range(T):
    N, K = [int(x) for x in input().split()]
    
    G = [[1, N]]
    
    while True:
        x, M = G.pop()
        if x >= K:
            break
        K -= x
        add_to_list(G, x, M//2)
        add_to_list(G, x, (M-1)//2)
    
    print("Case #{0}: {1} {2}".format(t+1, M//2, (M-1)//2))
    

