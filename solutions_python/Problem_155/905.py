T = int(input())


for t in range(T):
    Smax, audience = input().split()
    Smax = int(Smax)

    total = 0
    added = 0

    for S in range(Smax+1):
        if total < S:
            added += S - total
            total = S
        total += int(audience[S])

    print('Case #{}: {}'.format(t+1, added))


