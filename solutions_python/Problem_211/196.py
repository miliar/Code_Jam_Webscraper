T = int(input())

for t in range(T):
    N, K = list(map(int, input().split()))
    u = float(input())
    p = list(map(float, input().split()))
    p = sorted(p)
    p.append(1.)
    last_p = p[0]
    for i in range(1, N+1):
        dif = min(p[i] - last_p, u/i)
        u -= dif*i
        last_p += dif
        #print(dif, last_p)
        if u < 0.0000001 or i == N:
            for j in range(i):
                p[j] = last_p
            break

    p = p[:-1]
    ans = 1.
    for x in p:
        ans *= x

    print('Case #{0:d}: {1:.10f}'.format(t+1, ans))
