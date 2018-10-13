def time(D, K, S):
    return (D - K) / S

for i in range(int(raw_input())):
    D, N = map(int, raw_input().split())
    D = float(D)
    horses = []
    for _ in range(N):
        K, S = map(float, raw_input().split())
        horses.append((K, S))

    slowest = max(horses, key=lambda h: (D - h[0]) / h[1])
    sol = D / ((D - slowest[0]) / slowest[1])
    print 'Case #{0}: {1}'.format(i+1, sol)
