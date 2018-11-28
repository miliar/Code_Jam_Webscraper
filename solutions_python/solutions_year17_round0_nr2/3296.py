def tidyStep(N):
    d = list(str(N))
    for i in range(len(d)-1):
        if d[i] > d[i+1]:
            d = d[:i+1] + ['0']*(len(d)-i-1)
            return int(''.join(d))-1
    return int(''.join(d))

T = int(input())
for q in range(T):
    N = int(input())
    K = -1
    while K != N:
        K = N
        N = tidyStep(N)
    print("Case #" + str(q + 1) + ": " + str(K))