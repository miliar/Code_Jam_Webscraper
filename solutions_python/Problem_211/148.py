def zlepsi(a, b, c):
    l = max(0, b + c - 1)
    r = min(c, 1 - a)



T = int(input())
for tid in range(T):
    N, K = [int(x) for x in input().split(' ')]
    U = float(input())
    P = [float(x) for x in input().split(' ')]
    R = [0.0 for x in range(N)]
    # z = U
    # for i in range(N):
    #     R[i] = min(z, 1.0 - P[i])
    #     z -= R[i]
    #     if z <= 0.0:
    #         break
    P.sort(reverse = True)
    result = 1.0
    for r in range(K):
        priemer = (sum(P[r:]) + U)/(K-r)
        if P[r] > priemer:
            result *= P[r]
        else:
            result *= priemer**(K-r)
            break


    print('Case #{}: {}'.format(tid + 1, str(min(result, 1.0))))
