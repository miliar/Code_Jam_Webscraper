def solve(D, K, S):
    t = max((D-K[i])/S[i] for i in range(len(K)))
    return D/t

for T in range(int(input())):
    D, N = map(int,input().split())
    K = []
    S = []
    for i in range(N):
        a, b = map(int,input().split())
        K.append(a)
        S.append(b)
    print("Case #%d: %f"%(T+1, solve(D,K,S)))