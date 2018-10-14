T = int(input())
for t in range(1,T+1):
    P, K = input().split()
    P, K, N, A = '+'+P+'+', int(K), len(P), 0
    P = [ int(P[n] != P[n+1]) for n in range(N+1) ]
    for n in range(N-K+1): P[n], P[n+K], A = 0, (P[n+K]+P[n])%2, A+P[n]
    print('Case #{}: {}'.format(t,'IMPOSSIBLE' if sum(P) else A))
