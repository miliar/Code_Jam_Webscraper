def solve(k):
    k = list(str(k))
    for i in range(len(k)-1):
        if k[i] > k[i+1]:
            k = k[:i+1] + ['0']*(len(k)-i-1)
            return int(''.join(k)) -1
    return int(''.join(k))

T = int(input())
for i in range(T):
    K = int(input())
    n = False
    while n != K:
        n = K
        K = solve(K)
    print("Case #" + str(i+1) + ":", solve(K))