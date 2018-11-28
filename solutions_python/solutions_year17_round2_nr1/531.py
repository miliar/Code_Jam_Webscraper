T = int(input())
for tid in range(T):
    m = float(0)
    D, N = [int(x) for x in input().split(' ')]
    for i in range(N):
        k, s = [float(x) for x in input().split(' ')]
        m = max((D-k)/s, m)
    result = D/m
    print('Case #{}: {}'.format(tid + 1, str(result)))
