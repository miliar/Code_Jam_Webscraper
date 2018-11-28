T = int(input())
def f(N, K):
    if K==1:
        return (N/2, (N-1)/2)
    else:
        if K%2==0:
            return f(N/2, K/2)
        else:
            return f((N-1)/2, K/2)
for t in range(T):
    NK = raw_input().split()
    N, K = int(NK[0]), int(NK[1])
    w = f(N, K)
    print('Case #{}: {} {}'.format(t+1, *w))

