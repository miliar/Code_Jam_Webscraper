def rec(N,K):
    if K == 0:
        return (N, N)
    if K == 1:
        return ((N-1)//2, (N-1)//2 + (N-1)%2)
    else:
        if N%2 == 1:
            return rec(N//2, (K-1)//2 + (K-1)%2)
        else:
            return rec((N-1)//2 + (K-1)%2, (K-1)//2 + (K-1)%2)

T = int(input())
for j in range(T):
    N,K = input().split()
    N = int(N)
    K = int(K)
    out = rec(N,K)
    out1 = out[1]
    out2 = out[0]
    print("Case #{}:".format(j+1), out1, out2)
